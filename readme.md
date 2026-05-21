# AI-102 Training Repo


## Setting the local env

### Install python3

#### windows

if choco is not installed, in powershell
```
Get-ExecutionPolicy

Set-ExecutionPolicy AllSigned

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

choco -v
```

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

### Execute Image Analysis Script with harcode internet image

```
python .\aiscripts\01_image_analysis.py "noimage"
```