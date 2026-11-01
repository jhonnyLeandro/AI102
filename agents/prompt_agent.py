import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition
from dotenv import load_dotenv
load_dotenv()

AGENT_NAME = "IT-HelpDesk-Agent"

# authenticating with entra id
client = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

# creating the agent
agent = client.agents.create_version(
    agent_name=AGENT_NAME,
    definition=PromptAgentDefinition(
        model=os.environ["MODEL_DEPLOYMENT_NAME"],
        instructions=(
            "You are an IT support assistant for a company. "
            "Help users with password resets, VPN issues, and software installation. "
            "Give clear, step-by-step answers. "
            "If the question is outside IT support tpics, politely say so. "
        )
    )
)

print(f"Agent created:")
print(f"ID: {agent.id}")
print(f"Name: {agent.name}")
print(f"Version: {agent.version}")