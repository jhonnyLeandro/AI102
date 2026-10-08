import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

key = os.environ["LANGUAGE_SERVICE_KEY"]
endpoint = os.environ["LANGUAGE_SERVICE_ENDPOINT"] 
    
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
    
# Authenticate the client using your key and endpoint 
def authenticate_client():
     ta_credential = AzureKeyCredential(key)
     text_analytics_client = TextAnalyticsClient(
             endpoint=endpoint, 
             credential=ta_credential)
     return text_analytics_client
    
client = authenticate_client()
    
# Example method for detecting sensitive information (PII) from text 
def pii_recognition_example(client):
    documents = [
        "My name is John Smith and my phone number is 555-123-4567.",
        "Please send the invoice to maria.garcia@contoso.com. My credit card is 4111 1111 1111 1111.",
        "Patient Laura Gómez, born on 03/15/1985, lives at 123 Main Street, Seattle.",
        ]
    response = client.recognize_pii_entities(documents, language="en")
    result = [doc for doc in response if not doc.is_error]
    for doc in result:
        print("Redacted Text: {}".format(doc.redacted_text))
        for entity in doc.entities:
            print("Entity: {}".format(entity.text))
            print(" Category: {}".format(entity.category))
            print(" Confidence Score: {}".format(entity.confidence_score))
            print(" Offset: {}".format(entity.offset))
            print(" Length: {}".format(entity.length))

pii_recognition_example(client)