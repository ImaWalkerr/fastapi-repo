from typing import Dict
from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from src.models.twitch import Streams, StreamsResponse, StreamsUpdate
from src.di.container_general import ContainerGeneral
from src.di.container_dao import ContainerDAO
from src.di.container_parser import ContainerTwitch


class Stream:
    def __init__(self,
                 container_general: ContainerGeneral,
                 container_dao: ContainerDAO,
                 container_twitch: ContainerTwitch,
                 ):
        self.__container_general = container_general
        self.__container_dao = container_dao
        self.__container_twitch = container_twitch

    """calls for rest methods + http exceptions"""
    async def create_new_stream(self, streams: StreamsUpdate) -> Dict[str, str]:
        return await self.__container_dao.mongo_source.twitch_connection.streams_connection.create_new_stream(streams)

    async def get_streams(self) -> StreamsResponse:
        return await self.__container_dao.mongo_source.twitch_connection.streams_connection.get_streams()

    async def get_stream_by_id(self, id: str) -> Streams:
        try:
            return await self.__container_dao.mongo_source.twitch_connection.streams_connection.get_stream_by_id(id)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Stream with ID {id} not found')

    async def update_stream(self, id: str, streams: StreamsUpdate):
        try:
            await self.__container_dao.mongo_source.twitch_connection.streams_connection.update_stream(id, streams)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Stream with ID {id} not found')

    async def delete_stream(self, id: str):
        try:
            await self.__container_dao.mongo_source.twitch_connection.streams_connection.delete_stream(id)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Stream with ID {id} not found')
