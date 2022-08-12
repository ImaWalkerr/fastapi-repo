import aioredis
from fastapi import FastAPI

from src.config import Config, Redis


class ContainerGeneral:
    def __init__(self):
        self.__app = FastAPI()
        self.__config = Config()
        self.__redis = self.__init_redis()

    @property
    def app(self) -> FastAPI:
        return self.__app

    @property
    def config(self) -> Config:
        return self.__config

    @property
    def redis(self) -> Redis:
        return self.__redis

    def __init_redis(self) -> Redis:
        return aioredis.from_url(
            f'redis://{self.config.redis.host}',
            db=self.config.redis.db,
            encoding='utf8',
            decode_responces=True
        )
