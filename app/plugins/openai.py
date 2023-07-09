import openai
from langchain.embeddings.openai import OpenAIEmbeddings

from app.config import openai_settings


class OpenaiClient:
    def __init__(self):
        self.embed = OpenAIEmbeddings(
            client=openai,
            model=openai_settings.model,
            openai_api_key=openai_settings.api_key,
        )

    def embed_documents(self, documents: list[str]):
        return self.embed.embed_documents(documents)


openai_client = OpenaiClient()
