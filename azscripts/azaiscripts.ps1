$creds = Get-Content -Raw (Join-Path $PSScriptRoot "..\servicePrincipal.json") | ConvertFrom-Json

# login
az login --service-principal --username $creds.appId --password $creds.password --tenant $creds.tenant

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