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

openai = client.get_openai_client()

response = openai.responses.create(
    extra_body={"agent_reference":{"name": AGENT_NAME, "type": "agent_reference"}},
    input = "How do I reset my company password?"
)

print(response.output_text)