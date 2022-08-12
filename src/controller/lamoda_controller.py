from typing import Dict
from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from src.models.lamoda import Clothes, ClothesResponse, ClothesUpdate
from src.di.container_general import ContainerGeneral
from src.di.container_dao import ContainerDAO
from src.di.container_parser import ContainerParser


class Lamoda:
    def __init__(self,
                 container_general: ContainerGeneral,
                 container_dao: ContainerDAO,
                 container_parser: ContainerParser
                 ):
        self.__container_general = container_general
        self.__container_dao = container_dao
        self.__container_parser = container_parser

    """call lamoda parser"""
    async def run(self):
        await self.__container_parser.app.get_clothes_data()

    """calls for rest methods + http exceptions"""
    async def create_new_clothe(self, clothes: ClothesUpdate) -> Dict[str, str]:
        return await self.__container_dao.mongo_source.lamoda_connection.create_new_clothe(clothes)

    async def get_clothes(self) -> ClothesResponse:
        return await self.__container_dao.mongo_source.lamoda_connection.get_clothes()

    async def get_clothe_by_id(self, id: str) -> Clothes:
        try:
            return await self.__container_dao.mongo_source.lamoda_connection.get_clothe_by_id(id)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Clothe with ID {id} not found')

    async def update_clothe(self, id: str, clothes: ClothesUpdate):
        try:
            await self.__container_dao.mongo_source.lamoda_connection.update_clothe(id, clothes)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Clothe with ID {id} not found')

    async def delete_clothe(self, id: str):
        try:
            await self.__container_dao.mongo_source.lamoda_connection.delete_clothes(id)
        except Exception as e:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Clothe with ID {id} not found')
