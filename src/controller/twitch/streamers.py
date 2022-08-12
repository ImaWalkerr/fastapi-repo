from typing import Dict
from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from src.models.twitch import Streamers, StreamersResponse, StreamersUpdate
from src.di.container_general import ContainerGeneral
from src.di.container_dao import ContainerDAO
from src.di.container_parser import ContainerTwitch


class Streamer:
    def __init__(self,
                 container_general: ContainerGeneral,
                 container_dao: ContainerDAO,
                 container_twitch: ContainerTwitch,
                 ):
        self.__container_general = container_general
        self.__container_dao = container_dao
        self.__container_twitch = container_twitch

    """calls for rest methods + http exceptions"""
    async def create_new_streamer(self, streamers: StreamersUpdate) -> Dict[str, str]:
        return await self.__container_dao.mongo_source.twitch_connection.streamers_connection.create_new_streamer(
            streamers)

    async def get_streamers(self) -> StreamersResponse:
        return await self.__container_dao.mongo_source.twitch_connection.streamers_connection.get_streamers()

    async def get_streamer_by_id(self, id: str) -> Streamers:
        try:
            return await self.__container_dao.mongo_source.twitch_connection.streamers_connection.get_streamer_by_id(id)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Streamer with ID {id} not found')

    async def update_streamer(self, id: str, streamers: StreamersUpdate):
        try:
            await self.__container_dao.mongo_source.twitch_connection.streamers_connection.update_streamer(id, streamers)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Streamer with ID {id} not found')

    async def delete_streamer(self, id: str):
        try:
            await self.__container_dao.mongo_source.twitch_connection.streamers_connection.delete_streamer(id)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Game with ID {id} not found')