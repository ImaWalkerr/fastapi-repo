from src.controller import Lamoda, Twitch
from src.controller.twitch import Game, Stream, Streamer
from src.di.container_dao import ContainerDAO
from src.di.container_general import ContainerGeneral
from src.di.container_parser import ContainerParser, ContainerTwitch


class ContainerController:
    def __init__(self,
                 container_general: ContainerGeneral,
                 container_dao: ContainerDAO,
                 container_twitch: ContainerTwitch,
                 container_lamoda: ContainerParser
                 ):
        self.__container_general = container_general
        self.__container_dao = container_dao
        self.__container_twitch = container_twitch
        self.__container_lamoda = container_lamoda
        self._twitch_controller = None
        self._lamoda_controller = None
        self.__game_controller = None
        self.__stream_controller = None
        self.__streamer_controller = None

    @property
    def twitch_controller(self) -> Twitch:
        if self._twitch_controller is None:
            self._twitch_controller = Twitch(
                self.__container_general,
                self.__container_dao,
                self.__container_twitch,
                self.__game_controller,
                self.__stream_controller,
                self.__streamer_controller
            )
        return self._twitch_controller

    @property
    def lamoda_controller(self) -> Lamoda:
        if self._lamoda_controller is None:
            self._lamoda_controller = Lamoda(
                self.__container_general,
                self.__container_dao,
                self.__container_lamoda
            )
        return self._lamoda_controller

    @property
    def game_controller(self) -> Game:
        if self.__game_controller is None:
            self.__game_controller = Game(
                self.__container_general,
                self.__container_dao,
                self.__container_twitch
            )
        return self.__game_controller

    @property
    def stream_controller(self) -> Stream:
        if self.__stream_controller is None:
            self.__stream_controller = Stream(
                self.__container_general,
                self.__container_dao,
                self.__container_twitch
            )
        return self.__stream_controller

    @property
    def streamer_controller(self) -> Streamer:
        if self.__streamer_controller is None:
            self.__streamer_controller = Streamer(
                self.__container_general,
                self.__container_dao,
                self.__container_twitch
            )
        return self.__streamer_controller
