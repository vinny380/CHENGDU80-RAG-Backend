from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchIndex, SimpleField, SearchFieldDataType

# Azure Cognitive Search configuration
search_service_name = "dataqueens-search"  # e.g., "mysearchservice"
index_name = "test-index"  # e.g., "documents"
admin_key = "siHrN8wbjbYyFSjkBWqfvFGtx6ZFgfwDCcHOU1F0nbAzSeA9zlQJ"  # Your Azure search admin key

# Initialize Search Index Client
endpoint = f"https://{search_service_name}.search.windows.net"
index_client = SearchIndexClient(endpoint=endpoint, credential=admin_key)

# Initialize Search Client
search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=admin_key)

def create_index():
    try:
        # Define the index schema
        index = SearchIndex(
            name=index_name,
            fields=[
                SimpleField(name="id", type=SearchFieldDataType.String, key=True),
                SimpleField(name="content", type=SearchFieldDataType.String, searchable=True),
                SimpleField(name="title", type=SearchFieldDataType.String, searchable=True),
                SimpleField(name="embedding", type=SearchFieldDataType.Collection(SearchFieldDataType.Double))  # For embeddings
            ]
        )
        
        # Create the index
        index_client.create_index(index)
        print(f"Index created successfully!")
    except Exception as e:
        print(e)
        
def index_documents(documents):
    # Upload documents to the index
    result = search_client.upload_documents(documents=documents)
    print(f"Indexed documents: {result}")

def search_documents(search_text):
    # Perform a search query
    results = search_client.search(search_text)
    
    # Print the results
    for result in results:
        print(f"ID: {result['id']}, Title: {result['title']}, Content: {result['content']}")

def search_with_vector(query_embedding):
    # Search with vector similarity
    results = search_client.search(
        search_text="",
        vector=query_embedding,
        top=5  # Adjust as needed
    )
    
    # Print the results
    for result in results:
        print(f"ID: {result['id']}, Title: {result['title']}, Content: {result['content']}")

if __name__ == "__main__":
    # Create index
    create_index()
    
    # Example document
    document = {
        "id": "1",
        "content": "This is a sample document.",
        "title": "Sample Document",
        "embedding": [0.1, 0.2, 0.3]  # Example embedding vector
    }

    # Index documents
    index_documents([document])

    # Example search query
    print("Performing search for 'sample':")
    search_documents("sample")

    # Example vector for searching (replace with actual embedding)
    query_embedding = [0.1, 0.2, 0.3]
    print("Performing vector search:")
    search_with_vector(query_embedding)
