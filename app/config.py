from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PineconeSettings(BaseSettings):
    api_key: str = Field(default=...)
    environment: str = "us-central1-gcp"
    index: str = "testing-index"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="PINECONE_"
    )


pinecone_settings = PineconeSettings()
