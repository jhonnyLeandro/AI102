import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider


deployment_name = "gpt-4.1-mini"

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-03-01-preview",
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "Tell me about the ELIZA chatbot",
        }
    ],
)

response = client.responses.create(
    model=deployment_name,
    instructions="""
        You are a helpful AI assistant who supports employees with expense claims.
        Provide concise, accurate information only on topics related to expenses.
        Do not provide any information about topics that are not directly related to expenses.
    """,
    input="What kinds of business expense are typically reimbursed by employers?",
)

print(completion.choices[0].message)
print(response.output_text)