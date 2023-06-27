from pydantic import BaseSettings, Field


class DSL(BaseSettings):
    dbname: str = Field(env='POSTGRES_DB')
    user: str = Field(env='POSTGRES_USER')
    password: str = Field(env='POSTGRES_PASSWORD')
    host: str = Field(env='DB_HOST')
    port: int = Field(env='DB_PORT')
    options: str = '-c search_path=content'
    connect_timeout: int = 3


class Env(BaseSettings):
    debug: bool = Field(env='DEBUG') == 'True'
    secretkey: str = Field(env='SECRET_KEY')
    tokendelta: int = Field(env='ACCESS_TOKEN_EXPIRE_MINUTES')
