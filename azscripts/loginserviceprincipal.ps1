# get credentials
$creds = Get-Content -Raw (Join-Path $PSScriptRoot "..\servicePrincipal.json") | ConvertFrom-Json

Write-Host "Credentials : $creds"


# login
az login --service-principal `
    --username $creds.appId `
    --tenant $creds.tenant `
    --certificate $creds.fileWithCertAndPrivateKey  `
    --output none