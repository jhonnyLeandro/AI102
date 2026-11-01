import os
import json
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
from helpdesk_functions import run_local_function

load_dotenv()

AGENT_NAME = "IT-HelpDesk-Agent"
VERSION = "2"

# authenticating with entra id
project = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

client = project.get_openai_client()

conversation = client.conversations.create()

response = client.responses.create(
    conversation=conversation.id,
    input = "My VPN keeps disconnecting. What should I do?",
    extra_body={
        "agent_reference": {
            "type": "agent_reference",
            "name": AGENT_NAME,
            "version": VERSION
        }
    },
)

tool_outputs = []

for item in response.output:
    if item.type ==  "function_call":
        function_name = item.name
        arguments = json.loads(item.arguments)

        print(f"Function requested: {function_name}")
        print(f"Arguments received: {arguments}")

        function_result = run_local_function(function_name, arguments)
        tool_outputs.append(
            {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": function_result,
            }
        )

if tool_outputs:
    final_reponse = client.responses.create(
        conversation=conversation.id,
        input=tool_outputs,
        extra_body={
            "agent_reference":{
                "type": "agent_reference",
                "name": AGENT_NAME,
                "version": VERSION,
            }
        },
    )
    
    print(final_reponse.output_text)

else:
    print(response.output_text)