import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition, FunctionTool
from dotenv import load_dotenv
load_dotenv()

AGENT_NAME = "cloudxeus-support-rag-agent"

SYSTEM_PROMPT = """
You are a customer support assistant  for CloudXeus Technology Services.

Answer the customer's question using ONLY the provided sources.

After you answer, cite the source URL you used.

If the sources do not contain the answer, say:

"I don't have that information in the available knowledge base."

Then suggest  contacting support@cloudxeus.com

Never invent policies, prices, refund rules, or timelines


"""

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
        instructions=SYSTEM_PROMPT,
    )
)

print(f"Agent created:")
print(f"ID: {agent.id}")
print(f"Name: {agent.name}")
print(f"Version: {agent.version}")