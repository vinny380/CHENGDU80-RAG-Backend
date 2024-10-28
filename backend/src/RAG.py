import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchIndex,SearchableField, SimpleField,SearchField, SearchFieldDataType
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.models import VectorizedQuery
from azure.search.documents.indexes.models import (
    SimpleField,
    SearchFieldDataType,
    SearchableField,
    SearchField,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
    SemanticConfiguration,
    SemanticPrioritizedFields,
    SemanticField,
    SemanticSearch,
    SearchIndex,
    AzureOpenAIVectorizer
)
from imports import SEARCH_SERVICE_NAME, SEARCH_INDEX_NAME, SEARCH_ADMIN_KEY, SEARCH_ENDPOINT
import json


# Initialize the SearchIndexClient
index_client = SearchIndexClient(endpoint=SEARCH_ENDPOINT,
                                  credential=AzureKeyCredential(SEARCH_ADMIN_KEY))
# Initialize Search Client
search_client = SearchClient(endpoint=SEARCH_ENDPOINT, index_name=SEARCH_INDEX_NAME, credential=AzureKeyCredential(SEARCH_ADMIN_KEY))


def create_index():
    try:
        # Configure the vector search configuration  
        vector_search = VectorSearch(
            algorithms=[
                HnswAlgorithmConfiguration(
                    name="myHnsw"
                )
            ],
            profiles=[
                VectorSearchProfile(
                    name="myHnswProfile",
                    algorithm_configuration_name="myHnsw",
                    vectorizer="myVectorizer"
                )
            ]
        )

        # Define the index schema
        index = SearchIndex(
            name=SEARCH_INDEX_NAME,
            fields=[
                # SimpleField(name="id", type=SearchFieldDataType.String, key=True,sortable=True,filterable=True,facetable=True),
                SimpleField(name="auto_make", type=SearchFieldDataType.String),
                SimpleField(name="auto_model", type=SearchFieldDataType.String),
                SimpleField(name="vehicle_maker", type=SearchFieldDataType.String),
                SimpleField(name="vehicle_model", type=SearchFieldDataType.String),
                SimpleField(name="auto_year", type=SearchFieldDataType.Int32),
                SimpleField(name="vehicle_year", type=SearchFieldDataType.Int32),
                SimpleField(name="age", type=SearchFieldDataType.Int32),
                SimpleField(name="sex", type=SearchFieldDataType.String),
                SimpleField(name="education_level", type=SearchFieldDataType.String, key=True, filterable=True,facetable=True),
                SimpleField(name="relationship", type=SearchFieldDataType.String),
                SimpleField(name="previous_accidents_injuries", type=SearchFieldDataType.String),
                SimpleField(name="previous_accidents_conditions", type=SearchFieldDataType.String),
                SimpleField(name="previous_accidents_crash_speed", type=SearchFieldDataType.Double),
                SimpleField(name="liability_coverage_bodily_injury_liability_per_person", type=SearchFieldDataType.Int32),
                SimpleField(name="liability_coverage_bodily_injury_liability_per_accident", type=SearchFieldDataType.Int32),
                SimpleField(name="liability_coverage_property_damage_liability_per_accident", type=SearchFieldDataType.Int32),
                SimpleField(name="comprehensive_coverage_deductible", type=SearchFieldDataType.Int32),
                SimpleField(name="collision_coverage_included", type=SearchFieldDataType.Boolean),
                SimpleField(name="collision_coverage_deductible", type=SearchFieldDataType.Int32),
                SimpleField(name="personal_injury_protection_medical_expenses_limit", type=SearchFieldDataType.Int32),
                SimpleField(name="personal_injury_protection_lost_wages_limit", type=SearchFieldDataType.Int32),
                SimpleField(name="underinsured_motorist_coverage_bodily_injury_per_person", type=SearchFieldDataType.Int32),
                SimpleField(name="underinsured_motorist_coverage_bodily_injury_per_accident", type=SearchFieldDataType.Int32),
                SimpleField(name="underinsured_motorist_coverage_property_damage_per_accident", type=SearchFieldDataType.Int32),
                SimpleField(name="underinsured_motorist_coverage_deductible", type=SearchFieldDataType.Int32),
                SimpleField(name="av_specific_coverage_deductible", type=SearchFieldDataType.Int32),
                SimpleField(name="premium_details_annual_premium", type=SearchFieldDataType.Int32),
                SimpleField(name="premium_details_discounts", type=SearchFieldDataType.String),
                SimpleField(name="premium_details_payment_options", type=SearchFieldDataType.String),
                SearchField(name="embedding", type=SearchFieldDataType.Collection(SearchFieldDataType.Single), searchable=True, vector_search_dimensions=1536, vector_search_profile_name="myHnswProfile"),
                
                ],
            vector_search=vector_search,
        )
        
      
        #result = index_client.create_or_update_index(index)
        #print(f' {result.name} created')

        # Create the index
        index_client.delete_index(index)
        print(f"Index Deleted successfully!")
        index_client.create_index(index)
        print(f"Index created successfully!")


    except Exception as e:
        print(e)

def index_documents(documents):
    # Upload documents to the index
    result = search_client.upload_documents(documents=documents)
    #print(f"Indexed documents: {result}")
    return len(result)


def search_with_vector(query_embedding):
    vector_query = VectorizedQuery(vector=query_embedding, k_nearest_neighbors=3, fields="embedding")
  
    results = search_client.search(  
        search_text=None,  
        vector_queries= [vector_query],
        select=["title", "content"],
    )  
    
    #for result in results:  
    #    print(f"Title: {result['title']}")  
    #    print(f"Score: {result['@search.score']}")  
    #    print(f"Content: {result['content']}")   
    return results



if __name__ == "__main__":
    create_index()


    with open('documents_for_vector.json', 'r') as file:
        list_of_dict = json.load(file)

    index_documents(list_of_dict)


    # x = list_of_dict[3]
    # keys= x.keys()
    # for i in keys:
    #     print(i, type(x[i]))
    # # print(type(x["auto_make"]))
    # # index_documents(list_of_dict)
