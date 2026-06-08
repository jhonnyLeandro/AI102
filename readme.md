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

**linux**
.venv/bin/activate

**windows**
.venv\Scripts\Activate.ps1
```

### Install libraries

```
pip install --upgrade pip

or 

python.exe -m pip install --upgrade pip

pip install -r requirements.txt
```

[How to execute image analysis exercise](aiscripts/01_image_analysis.md)


[How to execute image model and agent exercise](run_model/run_agent_model.md)