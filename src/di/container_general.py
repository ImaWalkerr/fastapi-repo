import logging
import sys
import aioredis
from fastapi import FastAPI

from src.config import Config, Redis
from src.models.system import LogLevel


class ContainerGeneral:
    def __init__(self):
        self.__app = FastAPI()
        self.__config = Config()
        self.__redis = self.__init_redis()
        # self.logging = self.__logger
        # self.__logger = self.logging.Logger()

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

    # @property
    # def logger(self) -> logging.Logger:
    #     if self.__logger is None:
    #         log_levels = {
    #             'DEBUG': logging.DEBUG,
    #             'INFO': logging.INFO,
    #             'WARNING': logging.WARNING,
    #             'ERROR': logging.ERROR
    #         }
    #         log_level = log_levels[LogLevel.value.upper()]
    #         self.__logger = logging.getLogger('game_crawler_logger')
    #         self.__logger.setLevel(log_levels['INFO'])
    #         lc = logging.StreamHandler(sys.stdout)
    #         lc.setLevel(log_level)
    #         lc.setFormatter(
    #             logging.Formatter(
    #                 '[%(asctime)s][%(levelname)s]:%(message)s',
    #                 datefmt='%d/%m/%Y%H:%M:%S'
    #             )
    #         )
    #         self.__logger.addHandler(lc)
    #     return self.__logger
