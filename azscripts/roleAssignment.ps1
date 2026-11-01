. "$PSScriptRoot\readenv.ps1"

$rg = Get-Content -Raw (Join-Path $PSScriptRoot "..\rgdata.json") | ConvertFrom-Json
$creds = Get-Content -Raw (Join-Path $PSScriptRoot "..\servicePrincipal.json") | ConvertFrom-Json
$scope ="/subscriptions/$env:AZ_SUBSCRIPTION/resourceGroups/"+$rg.name

Write-Host $scope

az role assignment create `
  --assignee $creds.appId `
  --role "Search Index Data Reader" `
  --scope $scope
