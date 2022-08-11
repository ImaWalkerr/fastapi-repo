from fastapi import APIRouter, Body
from starlette.status import HTTP_201_CREATED
from src.models.twitch import Streams, StreamsUpdate, StreamsResponse
from src.di import di_controller_container


router = APIRouter()


"""Twitch streams methods """
@router.post('/', response_description='Create a new stream')
async def create_new_stream(streams: StreamsUpdate = Body(...)) -> Streams:
    return await di_controller_container.stream_controller.create_new_stream(streams)


@router.get('/', response_description='Get list of all streams')
async def get_streams_list() -> StreamsResponse:
    return await di_controller_container.stream_controller.get_streams()


@router.get('/{id}', response_description='Get stream by id')
async def get_stream_by_id(id: str) -> Streams:
    return await di_controller_container.stream_controller.get_stream_by_id(id)


@router.put('/{id}', status_code=HTTP_201_CREATED, response_description='Update a stream info')
async def update_stream(id: str, streams: StreamsUpdate = Body(...)):
    return await di_controller_container.stream_controller.update_stream(id, streams)


@router.delete('/delete', response_description='Delete a stream')
async def delete_stream(id: str):
    return await di_controller_container.stream_controller.delete_stream(id)
