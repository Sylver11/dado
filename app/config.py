from pydantic import BaseSettings, Field

# from pydantic_settings import BaseSettings, SettingsConfigDict


class PineconeSettings(BaseSettings):
    api_key: str = Field(default=...)
    environment: str = "us-central1-gcp"
    index: str = "testing"

    # model_config = SettingsConfigDict(
    #     env_file=".env", env_file_encoding="utf-8", env_prefix="PINECONE_"
    # )
    class Config(BaseSettings.Config):
        env_prefix = "PINECONE_"
        env_file = ".env"
        env_file_encoding = "utf-8"


class OpenaiSettings(BaseSettings):
    api_key: str = Field(default=...)
    model: str = "text-embedding-ada-002"

    class Config(BaseSettings.Config):
        env_prefix = "OPENAI_"
        env_file = ".env"
        env_file_encoding = "utf-8"


pinecone_settings = PineconeSettings()

openai_settings = OpenaiSettings()
