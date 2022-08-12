from fastapi import APIRouter, Body
from starlette.status import HTTP_201_CREATED
from src.di import di_controller_container
from src.models.lamoda import Clothes, ClothesUpdate, ClothesResponse


router = APIRouter()


"""Lamoda routers methods """
@router.post('/', response_description='Create a new clothe')
async def create_new_clothe(clothes: ClothesUpdate = Body(...)) -> Clothes:
    return await di_controller_container.lamoda_controller.create_new_clothe(clothes)


@router.get('/', response_description='Get list of all clothes')
async def get_clothes_list() -> ClothesResponse:
    return await di_controller_container.lamoda_controller.get_clothes()


@router.get('/{id}', response_description='Get clothe by id')
async def get_clothe_by_id(id: str) -> Clothes:
    return await di_controller_container.lamoda_controller.get_clothe_by_id(id)


@router.put('/{id}', status_code=HTTP_201_CREATED, response_description='Update a clothe info')
async def update_clothe(id: str, clothes: ClothesUpdate = Body(...)):
    return await di_controller_container.lamoda_controller.update_clothe(id, clothes)


@router.delete('/delete', response_description='Delete a clothe')
async def delete_clothe(id: str):
    return await di_controller_container.lamoda_controller.delete_clothe(id)
