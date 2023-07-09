import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone

TEXT_FIELD = "text"


class LangchainClient:
    def __init__(self, embed: OpenAIEmbeddings, index: pinecone.Index):
        self.embed = embed
        self.index = index
        self.vectorstore = Pinecone(self.index, self.embed.embed_query, TEXT_FIELD)

    def text_similarity_search(self, query: str):
        response = self.vectorstore.similarity_search(
            query, k=3  # our search query  # return 3 most relevant docs
        )
        return response
