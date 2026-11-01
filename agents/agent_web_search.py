import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition, WebSearchTool
from dotenv import load_dotenv
load_dotenv()

AGENT_NAME = "Web-Search-Lab-Agent"

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
        instructions = "You are a helpful assistant. Use web search to answer questions that require current information.",
        tools = [WebSearchTool()]
        
    )
)

print(f"Agent created:")
print(f"ID: {agent.id}")
print(f"Name: {agent.name}")
print(f"Version: {agent.version}")