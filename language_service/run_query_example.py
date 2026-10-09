import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables from .env file
load_dotenv()
endpoint = os.environ["BASE_OPENAI_ENDPOINT"] + os.environ["AZURE_OPENAI_ENDPOINT"] 
api_key = os.environ["API_KEY"]
deployment_name = os.environ["MODEL_DEPLOYMENT_NAME"]

# Create the client object
client = AzureOpenAI(
    base_url=endpoint,
    api_key=api_key,
    api_version="preview"
)

# Make a request using the client
message = client.responses.create(
    model=deployment_name,
    input="En que me puedes ayudar?",
)

# Print the results
print(f"Sentiment: {message.output[0]}")