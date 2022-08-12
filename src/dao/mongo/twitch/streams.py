from bson.objectid import ObjectId
from fastapi import Body
from typing import Dict
from src.models.twitch import Streams, StreamsResponse, StreamsUpdate
from src.models.errors import NoStreamsByThisIdError


class StreamsConnection:
    def __init__(self, db):
        self.__db = db

    """CRUD for twitch streams router"""
    async def create_new_stream(self, streams: StreamsUpdate = Body(...)) -> Dict[str, str]:
        new_stream = self.__db.db.streams.insert_one(streams)
        return {'_id': str(new_stream.inserted_id), **streams.dict()}

    async def get_streams(self) -> StreamsResponse:
        return StreamsResponse(streams=list(self.__db.db.streams.find(limit=100)))

    async def get_stream_by_id(self, id: str) -> Streams:
        if (data := self.__db.db.streams.find_one({'_id': ObjectId(id)})) is not None:
            data['_id'] = str(data['_id'])
            return data
        else:
            raise NoStreamsByThisIdError

    async def update_stream(self, id: str, streams: StreamsUpdate = Body(...)):
        streams_data = {k: v for k, v in streams.dict().items() if v is not None}

        if len(streams_data) >= 1:
            update_stream = self.__db.db.streams.update_one(
                {"_id": ObjectId(id)}, {'$set': streams_data}
            )
            if update_stream.modified_count == 0:
                raise NoStreamsByThisIdError

    async def delete_stream(self, id: str):
        return self.__db.db.streams.delete_one({'_id': ObjectId(id)})
