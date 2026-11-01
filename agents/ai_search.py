from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient

search_client = SearchClient(
    endpoint="https://mi-servicio-aisearch-01.search.windows.net",
    index_name="rag-1793320125623",
    credential=DefaultAzureCredential()
)


results = search_client.search(
    search_text = "cambio de clave",
    select=["chunk","title"],
)


for result in results:
    print(f"Score: {result['@search.score']:.4f}")
    print(f"Source: {result['title']}")
    print(f"Text: {result['chunk']}")
    print("----")