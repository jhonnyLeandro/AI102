# 1. Sign in and pick your subscription
az login --use-device-code

# 2. Variables (storage account names: 3-24 chars, lowercase letters/numbers, globally unique)
$RG = "rg-ai102-study"
$LOCATION = "eastus"
$STORAGE = "sthelpdeskrag$RANDOM"
$CONTAINER = "helpdesk-docs"

# 3. Resource group
# az group create --name $RG --location $LOCATION

# 4. Storage account
az storage account create  `
  --name $STORAGE `
  --resource-group $RG `
  --location $LOCATION `
  --sku Standard_LRS `
  --kind StorageV2 `
  --min-tls-version TLS1_2 `
  --allow-blob-public-access false


# 5. Give yourself data-plane access (needed for --auth-mode login)
$USER_ID    = az ad signed-in-user show --query id -o tsv
$STORAGE_ID = az storage account show -n $STORAGE -g $RG --query id -o tsv

az role assignment create `
  --assignee $USER_ID `
  --role "Storage Blob Data Contributor" `
  --scope $STORAGE_ID

# 6. Container (the role can take 1-2 minutes to propagate; retry if you get a 403)
az storage container create `
  --name $CONTAINER `
  --account-name $STORAGE `
  --auth-mode login

# 7. Upload the .md files from the current folder
<# az storage blob upload-batch `
  --destination $CONTAINER `
  --source . `
  --pattern "*.md" `
  --account-name $STORAGE `
  --auth-mode login #>

# 8. Verify
az storage blob list -c $CONTAINER --account-name $STORAGE --auth-mode login -o table
echo "Storage account: $STORAGE"