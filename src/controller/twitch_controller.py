from src.controller.twitch import Game, Stream, Streamer
from src.di.container_general import ContainerGeneral
from src.di.container_dao import ContainerDAO
from src.di.container_parser import ContainerTwitch


class Twitch:
    def __init__(self,
                 container_general: ContainerGeneral,
                 container_dao: ContainerDAO,
                 container_twitch: ContainerTwitch,
                 game_controller: Game,
                 stream_controller: Stream,
                 streamer_controller: Streamer
                 ):
        self.__container_general = container_general
        self.__container_dao = container_dao
        self.__container_twitch = container_twitch
        self.__game_controller = game_controller
        self.__stream_controller = stream_controller
        self.__streamer_controller = streamer_controller

    """call twitch api parser"""
    async def run(self):
        await self.__container_twitch.app.parse_twitch()
