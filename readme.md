# AI-102 Training Repo


## Setting the local env

### Install python3

#### windows

*if choco is not installed, in powershell*

```
Get-ExecutionPolicy

Set-ExecutionPolicy AllSigned

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

choco -v
```

*install python*

```
choco install python
```

#### linux

```
sudo apt update

sudo apt install python3

sudo apt install python3-pip
```

### Create work folder and python env

```
mkdir ai102-study && cd ai102-study

python -m venv .venv

.venv/bin/activate
```

### Install libraries

```
pip install --upgrade pip

pip install -r requirements.txt
```

### azure env

*login to azure with azure cli and create a resource group*

```
az group create 
--name rg-ai102-study `
--location eastus
```
*Create a multiservice cognitiveservice account*

```
az cognitiveservices account create `
  --name ai102-multiservice `
  --resource-group rg-ai102-study `
  --kind CognitiveServices `
  --sku S0 `
  --location eastus `
  --yes
```

*create a .env file and add endpoint and key*

*.env*
```
AZURE_AI_ENDPOINT=<ENDPOINT>
AZURE_AI_KEY=<KEY>
```

*using these commands*
```
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
```


## Image Analysis


### Execute Image Analysis Script with local image

```
python .\aiscripts\01_image_analysis.py   ".\images\leon.jpg"
```

```
python .\aiscripts\01_image_analysis.py   ".\images\me.jpg"
```

```
python .\aiscripts\01_image_analysis.py   ".\images\CasaSevilla.jpg"
```

### Execute Image Analysis Script with harcoded internet image

```
python .\aiscripts\01_image_analysis.py "noimage"
```