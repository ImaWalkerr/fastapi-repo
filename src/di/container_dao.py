import json
import pymongo
from typing import Union
from src.di.container_general import ContainerGeneral
from src.dao.mongo_main import Mongo
# from confluent_kafka import Producer


class ContainerDAO:
    def __init__(self, container_general: ContainerGeneral):
        self.__container_general = container_general
        self._mongo_source = None

    @property
    def mongo_source(self) -> Mongo:
        dsn = f'mongodb://{self.__container_general.config.mongodb.username}:' \
              f'{self.__container_general.config.mongodb.password}@{self.__container_general.config.mongodb.host}:' \
              f'{self.__container_general.config.mongodb.port}'
        connection = pymongo.MongoClient(dsn)
        return Mongo(connection)

    # @property
    # def kafka_source(self) -> Kafka:
    #     producer = KafkaProducer(
    #         bootstrap_servers=self.__container_general.config.kafka.inter_broker_listener_name,
    #         value_serializer=lambda v: json.dumps(v).encode('utf-8')
    #     )
    #     return Kafka(producer)
