import os
import base64
import mimetypes
from pathlib import Path
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# load env variables
load_dotenv()

# authenticate the client
client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-03-01-preview",
)

# reading the image to send into the model

image=input("entra el nombre de la imagen (leon, CasaSevilla, me) \n")
image_path = Path(__file__).parent.parent.parent / "images" / f"{image}.jpg "

mime = mimetypes.guess_type(image_path)[0] or "image/jpeg"
b64 = base64.b64encode(image_path.read_bytes()).decode("utf-8")
data_uri = f"data:{mime};base64,{b64}"


# ask the question
response = client.responses.create(
    model=os.getenv("MODEL_DEPLOYMENT_NAME"),  # your deployment name 
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What is in this image? Provide 3 bullet points."},
                {"type": "input_image", "image_url": data_uri}
            ],
        }
    ],
)

print(response.output_text)
