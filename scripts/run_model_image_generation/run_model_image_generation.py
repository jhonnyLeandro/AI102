import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

# load env variables
load_dotenv()

# get image generation model name
imageModel = os.environ["IMAGE_GENERATION_MODEL"]

# authenticate the client
client = OpenAI(
    api_key=os.environ["API_KEY"],
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"].rstrip("/") + "/openai/v1/",
    default_headers={"x-ms-oai-image-generation-deployment": imageModel},
)

prompt = input("Ingresa que imagen quieres crear \n")

response = client.responses.create(
    model= os.getenv("MODEL_DEPLOYMENT_NAME"),  # your deployment name in Foundry
    input=prompt,
    tools=[{"type": "image_generation"}],
)

image_base64 = next(
    item.result for item in response.output
    if item.type == "image_generation_call"
)

with open("foundry_generated.png", "wb") as f:
    f.write(base64.b64decode(image_base64))

print("Saved: foundry_generated.png")