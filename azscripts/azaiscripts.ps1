
# login 
az login --use-device-code

# create a resource group
az group create --name rg-ai102-study --location eastus

# create a cognitiveservices account
az cognitiveservices account create `
  --name ai102-multiservice `
  --resource-group rg-ai102-study `
  --kind CognitiveServices `
  --sku S0 `
  --location eastus `
  --yes


# Endpoint
az cognitiveservices account show `
  --name ai102-multiservice `
  --resource-group rg-ai102-study `
  --query properties.endpoint -o tsv

# Key
az cognitiveservices account keys list `
  --name ai102-multiservice `
  --resource-group rg-ai102-study `
  --query key1 -o tsv