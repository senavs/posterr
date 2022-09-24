from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    DATABASE_URI: str
    DATABASE_RESET: bool = False


class DeploySettings(BaseSettings):
    DEPLOY_HOST: str = "0.0.0.0"
    DEPLOY_PORT: int = 8888
    DEPLOY_DEBUG: bool = False
    DEPLOY_RELOAD: bool = False
    DEPLOY_ACCESS_LOG: bool = False


database = DatabaseSettings()
deploy = DeploySettings()
