# run Agent and Model Exercise

## Set up environment

- Go to Microsoft Foundry
- Create a Project
- Deploy model "gpt-4.1-mini", model script will be executed against this
- Add a Custom Instruction and  save model as an agent

## Login to Azure with azure cli for run agent script

```
az login --use-device-code
```

## execute script run_agent.py

```
 python run_model/run_agent.py
```

## Create a .env file to execute the run_model.py script

```
AZURE_OPENAI_ENDPOINT=<AZURE_OPENAI_ENDPOINT> # used in run_model.py
AZURE_OPENAI_API_KEY=<AZURE_OPENAI_API_KEY> # used in run_model.py
PROJECT_ENDPOINT=<PROJECT_ENDPOINT> # used in run_agent.py
```

## Excecute run_model.py script

```
python run_model/run_model.py
```