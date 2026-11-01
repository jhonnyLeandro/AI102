import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

load_dotenv()

deployment_name = os.environ["MODEL_DEPLOYMENT_NAME"] 

client = AzureOpenAI(
    azure_endpoint = os.environ["BASE_OPENAI_ENDPOINT"],
    api_key = os.environ["API_KEY"],
    api_version="2025-03-01-preview",
)

response = client.responses.create(
    model=deployment_name,
    instructions="""
        You are a helpful research assistant. Always cite your sources.
    """,
    input="what are the latest developments in AI regulation in the european union?",
    tools=[{"type": "web_search"}],
    tool_choice="auto"
)

print(f"Answer:  {response.output_text}")