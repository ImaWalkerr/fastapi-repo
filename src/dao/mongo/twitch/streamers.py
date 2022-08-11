from bson.objectid import ObjectId
from fastapi import Body
from typing import Dict
from src.models.twitch import Streamers, StreamersResponse, StreamersUpdate
from src.models.errors import NoStreamersByThisIdError


class StreamersConnection:
    def __init__(self, db):
        self.__db = db

    """CRUD for twitch streamers router"""
    async def create_new_streamer(self, streamers: StreamersUpdate = Body(...)) -> Dict[str, str]:
        new_streamer = self.__db.db.streamers.insert_one(streamers)
        return {'_id': str(new_streamer.inserted_id), **streamers.dict()}

    async def get_streamers(self) -> StreamersResponse:
        return StreamersResponse(streamers=list(self.__db.db.streamers.find(limit=100)))

    async def get_streamer_by_id(self, id: str) -> Streamers:
        if (data := self.__db.db.streamers.find_one({'_id': ObjectId(id)})) is not None:
            data['_id'] = str(data['_id'])
            return data
        else:
            raise NoStreamersByThisIdError

    async def update_streamer(self, id: str, streamers: StreamersUpdate = Body(...)):
        streamers_data = {k: v for k, v in streamers.dict().items() if v is not None}

        if len(streamers_data) >= 1:
            update_streamer = self.__db.db.streamers.update_one(
                {"_id": ObjectId(id)}, {'$set': streamers_data}
            )
            if update_streamer.modified_count == 0:
                raise NoStreamersByThisIdError

    async def delete_streamer(self, id: str):
        return self.__db.db.streamers.delete_one({'_id': ObjectId(id)})
