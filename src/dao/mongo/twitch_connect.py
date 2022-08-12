from src.dao.mongo.twitch import GamesConnection, StreamsConnection, StreamersConnection


class TwitchConnection:
    def __init__(self, db):
        self.__db = db
        self.__games = GamesConnection(self.__db)
        self.__streams = StreamsConnection(self.__db)
        self.__streamers = StreamersConnection(self.__db)

    @property
    def games_connection(self) -> GamesConnection:
        return self.__games

    @property
    def streams_connection(self) -> StreamsConnection:
        return self.__streams

    @property
    def streamers_connection(self) -> StreamersConnection:
        return self.__streamers
