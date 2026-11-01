import os
import base64
from pathlib import Path
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




BASE_DIR = Path(__file__).resolve().parent      
image_path = BASE_DIR.parent / "receipts" / "factura.jpg"  

with open(image_path, "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")


response = client.responses.create(
    model=deployment_name,
    instructions="""
        You are a helpful assistant that reads and extracts information from images.
    """,
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "image_url":f"data:image/png;base64,{image_data}"
                },
                {
                    "type":"input_text",
                    "text":"Extract all the text from this image and present it in a structured, readable format."
                }
            ]
        }
    ]
)


print(response.output_text)