from src.dao.mongo.twitch_connect import TwitchConnection
from src.dao.mongo.lamoda_connect import LamodaConnection


class Mongo:
    def __init__(self, db):
        self.__db = db
        self.__lamoda = LamodaConnection(self.__db)
        self.__twitch = TwitchConnection(self.__db)

    @property
    def lamoda_connection(self) -> LamodaConnection:
        return self.__lamoda

    @property
    def twitch_connection(self) -> TwitchConnection:
        return self.__twitch

    """For Lamoda parser"""
    def insert_clothes(self, clothes):
        return self.__db.db.lamoda.insert_many(clothes)

    """For Twitch api parser"""
    def insert_games(self, games):
        return self.__db.db.games.insert_many(games)

    def insert_streamers(self, streamers):
        return self.__db.db.streamers.insert_many(streamers)

    def insert_streams(self, streams):
        return self.__db.db.streams.insert_many(streams)
