. "$PSScriptRoot\readenv.ps1"

# Test your variables
Write-Host "Your API Key is: $env:AZ_SUBSCRIPTION"
# login 
az login --use-device-code

az ad sp create-for-rbac --name myServiePrincipalFoundry --role Contributor --scopes  /subscriptions/$env:AZ_SUBSCRIPTION