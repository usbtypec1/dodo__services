import pathlib
from functools import lru_cache

from pydantic import BaseSettings, Field
from dotenv import load_dotenv

__all__ = (
    'get_app_settings',
    'get_stocks_balance_settings',
    'ROOT_PATH',
    'LOGS_FILE_PATH',
    'LOCAL_STORAGE_PATH'
)

load_dotenv()

ROOT_PATH = pathlib.Path(__file__).parent.parent
LOGS_FILE_PATH = ROOT_PATH / 'logs.log'
LOCAL_STORAGE_PATH = ROOT_PATH / 'local_storage'


class AppSettings(BaseSettings):
    debug: bool = Field(..., env='DEBUG')
    api_url: str = Field(..., env='API_URL')
    db_api_url: str = Field(..., env='DB_API_URL')
    rabbitmq_url: str = Field(..., env='RABBITMQ_URL')


class StocksBalanceSettings(BaseSettings):
    days_left_threshold: int = Field(..., env='STOCKS_BALANCE_DAYS_LEFT_THRESHOLD')


@lru_cache
def get_app_settings() -> AppSettings:
    return AppSettings()


@lru_cache
def get_stocks_balance_settings() -> StocksBalanceSettings:
    return StocksBalanceSettings()
