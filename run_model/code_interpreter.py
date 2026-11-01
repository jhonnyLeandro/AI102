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
        You are a data analyst. Use python to calculate precisely.
    """,
    input="What is the compound interest on $10000 at 5 percent annual rate over 10 years",
    tools=[{"type": "code_interpreter", "container":{"type": "auto"}}]
)


for item in response.output:
    if item.type == "code_interpreter_call":
        print("=== Python Code the Model Wrote ===")
        print(item.code)
        print("\n=== Output from execution ===")
        print(item.outputs)
    elif item.type == "message":
        print("\n=== Final Answer ===")
        print(response.output_text)