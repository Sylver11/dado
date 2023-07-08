import pinecone

from app.config import pinecone_settings

pinecone.init(
    api_key=pinecone_settings.api_key, environment=pinecone_settings.environment
)
index = pinecone.Index(pinecone_settings.index)
