from fastapi import APIRouter, Body
from starlette.status import HTTP_201_CREATED
from src.models.twitch import Streamers, StreamersResponse, StreamersUpdate
from src.di import di_controller_container


router = APIRouter()


"""Twitch streamers methods """
@router.post('/', response_description='Create a new streamer')
async def create_new_streamer(streamers: StreamersUpdate = Body(...)) -> Streamers:
    return await di_controller_container.streamer_controller.create_new_streamer(streamers)


@router.get('/', response_description='Get list of all streamers')
async def get_streamers_list() -> StreamersResponse:
    return await di_controller_container.streamer_controller.get_streamers()


@router.get('/{id}', response_description='Get streamer by id')
async def get_streamer_by_id(id: str) -> Streamers:
    return await di_controller_container.streamer_controller.get_streamer_by_id(id)


@router.put('/{id}', status_code=HTTP_201_CREATED, response_description='Update a streamer info')
async def update_streamer(id: str, streamers: StreamersUpdate = Body(...)):
    return await di_controller_container.streamer_controller.update_streamer(id, streamers)


@router.delete('/delete', response_description='Delete a streamer')
async def delete_streamer(id: str):
    return await di_controller_container.streamer_controller.delete_streamer(id)
