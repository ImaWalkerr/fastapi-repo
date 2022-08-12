from typing import Dict
from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from src.models.twitch import Games, GamesResponse, GamesUpdate
from src.di.container_general import ContainerGeneral
from src.di.container_dao import ContainerDAO
from src.di.container_parser import ContainerTwitch


class Game:
    def __init__(self,
                 container_general: ContainerGeneral,
                 container_dao: ContainerDAO,
                 container_twitch: ContainerTwitch,
                 ):
        self.__container_general = container_general
        self.__container_dao = container_dao
        self.__container_twitch = container_twitch

    """calls for rest methods + http exceptions"""
    async def create_new_game(self, games: GamesUpdate) -> Dict[str, str]:
        return await self.__container_dao.mongo_source.twitch_connection.games_connection.create_new_game(games)

    async def get_games(self) -> GamesResponse:
        return await self.__container_dao.mongo_source.twitch_connection.games_connection.get_games()

    async def get_game_by_id(self, id: str) -> Games:
        try:
            return await self.__container_dao.mongo_source.twitch_connection.games_connection.get_game_by_id(id)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Game with ID {id} not found')

    async def update_clothe(self, id: str, games: GamesUpdate):
        try:
            await self.__container_dao.mongo_source.twitch_connection.games_connection.update_game(id, games)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Game with ID {id} not found')

    async def delete_game(self, id: str):
        try:
            await self.__container_dao.mongo_source.twitch_connection.games_connection.delete_games(id)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Game with ID {id} not found')