. "$PSScriptRoot\readenv.ps1"
$rg = Get-Content -Raw (Join-Path $PSScriptRoot "..\rgdata.json") | ConvertFrom-Json

# Definir variables de configuración
$subscriptionId = $env:AZ_SUBSCRIPTION
$resourceGroup  = $rg.name
$location       = "eastus"
$searchName     = "mi-servicio-aisearch-01"
$sku            = "basic" # Opciones comunes: free, basic, standard, standard2, standard3

# 1. Iniciar sesión en Azure (si no lo has hecho)
az login

# 2. Seleccionar la suscripción activa
az account set --subscription $subscriptionId

# 4. Crear el servicio de Azure AI Search
Write-Host "Creando servicio de Azure AI Search..." -ForegroundColor Cyan
az search service create `
    --name $searchName `
    --resource-group $resourceGroup `
    --sku $sku `
    --location $location `
    --partition-count 1 `
    --replica-count 1

Write-Host "¡Servicio creado con éxito!" -ForegroundColor Green
