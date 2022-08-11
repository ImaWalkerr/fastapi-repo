from bson.objectid import ObjectId
from fastapi import Body
from typing import Dict
from src.models.twitch import Games, GamesResponse, GamesUpdate
from src.models.errors import NoGamesByThisIdError


class GamesConnection:
    def __init__(self, db):
        self.__db = db

    """CRUD for twitch games router"""
    async def create_new_game(self, games: GamesUpdate = Body(...)) -> Dict[str, str]:
        new_game = self.__db.db.games.insert_one(games)
        return {'_id': str(new_game.inserted_id), **games.dict()}

    async def get_games(self) -> GamesResponse:
        return GamesResponse(games=list(self.__db.db.games.find(limit=100)))

    async def get_game_by_id(self, id: str) -> Games:
        if (data := self.__db.db.games.find_one({'_id': ObjectId(id)})) is not None:
            data['_id'] = str(data['_id'])
            return data
        else:
            raise NoGamesByThisIdError

    async def update_game(self, id: str, games: GamesUpdate = Body(...)):
        games_data = {k: v for k, v in games.dict().items() if v is not None}

        if len(games_data) >= 1:
            update_game = self.__db.db.games.update_one(
                {"_id": ObjectId(id)}, {'$set': games_data}
            )
            if update_game.modified_count == 0:
                raise NoGamesByThisIdError

    async def delete_games(self, id: str):
        return self.__db.db.games.delete_one({'_id': ObjectId(id)})
