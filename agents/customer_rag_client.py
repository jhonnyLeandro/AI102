import os
import json
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizableTextQuery

load_dotenv()

SEARCH_ENDPOINT = "https://mi-servicio-aisearch-01.search.windows.net"
INDEX_NAME = "rag-1793320125623"
AGENT_NAME = "cloudxeus-support-rag-agent"
VERSION = "1"


# authenticating with entra id
project = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

client = project.get_openai_client()

# search documents with azure ai search
search_client = SearchClient(
    endpoint="https://mi-servicio-aisearch-01.search.windows.net",
    index_name="rag-1793320125623",
    credential=DefaultAzureCredential()
)

def ask(question):
    # step 1: Retrieve grounding data from azure AI search
    results = search_client.search(
        search_text=question,
        vector_queries=[
            VectorizableTextQuery(
                text=question,
                k_nearest_neighbors=3,
                fields="text_vector"
            )
        ],
        select=["chunk", "title", "parent_id"],
        top=3,
    )

    # step 2: Convert search results into source text

    source_list = []

    for result in results:
        title = result.get("title", "Unknown source")
        parent_id = result.get("parent_id", "")
        chunk = result.get("chunk", "")

        source_text = f"""
[Source title: {title}]
[parent ID: {parent_id}]

{chunk}
"""
        source_list.append(source_text)

    sources = "\n\n".join(source_list)

    # Step 3: Build the grounded prompt for the agent

    prompt = f"""
You are  a customer support agent for CloudXeus Technology Services.

Answer the customer question using only the sources provided below.
If the sources do not contain enough information, say that the knowledge base does not contain enough information.


Sources: 

{sources}

Customer question:
{question}
"""
    print("\nprompt sent to agent:\n")
    print(prompt)

    # Step 4: Ask the Foundry agent to answer using the sources
    response = client.responses.create(
        extra_body={
            "agent_reference":{
                "name":AGENT_NAME,
                "type": "agent_reference"
            }
        },
        input=prompt,
    )
    return response.output_text


print(ask("Can i get my money back?"))