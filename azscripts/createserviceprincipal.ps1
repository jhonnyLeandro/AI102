. "$PSScriptRoot\readenv.ps1"

# Test your variables
Write-Host "Your API Key is: $env:AZ_SUBSCRIPTION"

$rg = Get-Content -Raw (Join-Path $PSScriptRoot "..\rgdata.json") | ConvertFrom-Json

$creds = Get-Content -Raw (Join-Path $PSScriptRoot "..\servicePrincipal.json") | ConvertFrom-Json

Write-Host "Credentials : $creds"

$scope = "/subscriptions/$env:AZ_SUBSCRIPTION/resourceGroups/"+$rg.name+"/providers/Microsoft.CognitiveServices/accounts/"+$rg.foundryProject
$scoperg = "/subscriptions/$env:AZ_SUBSCRIPTION/resourceGroups/"+$rg.name

Write-Host "Your Scope is: $scope"
Write-Host "Your Scope rg is: $scoperg"

# login 
az login --use-device-code

# create a service principal for foundry user 
az ad sp create-for-rbac --name myServiePrincipalFoundry --role Contributor --scopes  $scoperg --create-cert


<# # assign role foundry user to the service principal
az role assignment create --assignee-object-id $creds.appId `
                          --assignee-principal-type ServicePrincipal `
                          --role "Foundry User" `
                          --scope $scope


az role assignment create `
  --assignee $creds.appId `
  --role "Storage Blob Data Contributor" `
  --scope $scoperg #>



# delete role
<# $SUB_ID = az account show --query id -o tsv

az role assignment delete `
  --assignee $creds.appId  `
  --role "Contributor" `
  --scope "/subscriptions/$SUB_ID" #>