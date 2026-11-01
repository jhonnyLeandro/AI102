# login with service principal
. "$PSScriptRoot\readenv.ps1"
. "$PSScriptRoot\loginserviceprincipal.ps1"

# create a resource group
az group create --name rg-ai103-study --location eastus

# create a cognitiveservices account
az cognitiveservices account create `
  --name ai103-multiservice `
  --resource-group rg-ai103-study `
  --kind CognitiveServices `
  --sku S0 `
  --location eastus `
  --yes


# Endpoint
az cognitiveservices account show `
  --name ai103-multiservice `
  --resource-group rg-ai103-study `
  --query properties.endpoint -o tsv

# Key
az cognitiveservices account keys list `
  --name ai103-multiservice `
  --resource-group rg-ai103-study `
  --query key1 -o tsv 