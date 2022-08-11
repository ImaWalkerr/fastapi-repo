from fastapi import APIRouter, Body
from starlette.status import HTTP_201_CREATED
from src.models.twitch import Games, GamesUpdate, GamesResponse
from src.di import di_controller_container


router = APIRouter()


"""Twitch games methods """
@router.post('/', response_description='Create a new game')
async def create_new_game(games: GamesUpdate = Body(...)) -> Games:
    return await di_controller_container.game_controller.create_new_game(games)


@router.get('/', response_description='Get list of all games')
async def get_games_list() -> GamesResponse:
    return await di_controller_container.game_controller.get_games()


@router.get('/{id}', response_description='Get game by id')
async def get_game_by_id(id: str) -> Games:
    return await di_controller_container.game_controller.get_games_by_id(id)


@router.put('/{id}', status_code=HTTP_201_CREATED, response_description='Update a game info')
async def update_game(id: str, games: GamesUpdate = Body(...)):
    return await di_controller_container.game_controller.update_game(id, games)


@router.delete('/delete', response_description='Delete a game')
async def delete_game(id: str):
    return await di_controller_container.game_controller.delete_game(id)
