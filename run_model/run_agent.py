# Before running the sample:
#    pip install azure-ai-projects>=2.1.0
import os
from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

load_dotenv()

project_client = AIProjectClient(
    endpoint = os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

my_agent = "expenses-agent"
my_version = "2"

openai_client = project_client.get_openai_client()

# Reference the agent to get a response
response = openai_client.responses.create(
    input=[{"role": "user", "content": "Tell me what you can help with."}],
    extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
)

print(f"Response output: {response.output_text}")



