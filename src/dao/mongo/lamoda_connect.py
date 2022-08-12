from bson.objectid import ObjectId
from fastapi import Body
from typing import Dict
from src.models.lamoda import Clothes, ClothesResponse, ClothesUpdate
from src.models.errors import NoClothesByThisIdError


class LamodaConnection:
    def __init__(self, db):
        self.__db = db

    """CRUD for lamoda router"""
    async def create_new_clothe(self, clothes: ClothesUpdate = Body(...)) -> Dict[str, str]:
        new_clothe = self.__db.db.lamoda.insert_one(clothes)
        return {'_id': str(new_clothe.inserted_id), **clothes.dict()}

    async def get_clothes(self) -> ClothesResponse:
        return ClothesResponse(clothes=list(self.__db.db.lamoda.find(limit=100)))

    async def get_clothe_by_id(self, id: str) -> Clothes:
        if (data := self.__db.db.lamoda.find_one({'_id': ObjectId(id)})) is not None:
            data['_id'] = str(data['_id'])
            return data
        else:
            raise NoClothesByThisIdError

    async def update_clothe(self, id: str, clothes: ClothesUpdate = Body(...)):
        clothes_data = {k: v for k, v in clothes.dict().items() if v is not None}

        if len(clothes_data) >= 1:
            update_clothe = self.__db.db.lamoda.update_one(
                {"_id": ObjectId(id)}, {'$set': clothes_data}
            )
            if update_clothe.modified_count == 0:
                raise NoClothesByThisIdError

    async def delete_clothes(self, id: str):
        return self.__db.db.lamoda.delete_one({'_id': ObjectId(id)})
