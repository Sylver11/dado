from app.plugins.langchain import LangchainClient
from app.plugins.openai import openai_client
from app.plugins.pinecone import pinecone_client

# pinecone_client.populate_index(openai_client.embed)


langchain_client = LangchainClient(openai_client.embed, pinecone_client.index)

query = "who was Benito Mussolini?"
response = langchain_client.text_similarity_search(query)

print(response)
