from src.di.container_dao import ContainerDAO
from src.di.container_general import ContainerGeneral
from src.parsers.twitch_api import TwitchWrapper
from src.parsers.lamoda_parser import ParseLamoda


class ContainerTwitch:
    def __init__(self, container_general: ContainerGeneral, container_dao: ContainerDAO):
        self.__container_general = container_general
        self.__container_dao = container_dao

    @property
    def app(self) -> TwitchWrapper:
        return TwitchWrapper(self.__container_general, self.__container_dao)


class ContainerParser:
    def __init__(self, container_general: ContainerGeneral, container_dao: ContainerDAO):
        self._container_general = container_general
        self._container_dao = container_dao

    @property
    def app(self) -> ParseLamoda:
        return ParseLamoda(self._container_general, self._container_dao)
