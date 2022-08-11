from typing import Optional, List
from pydantic import BaseModel, Field, validator
from src.models.validators.object_id import object_id_to_string


class Streams(BaseModel):
    id: str = Field(..., alias="_id")
    stream_id: str = Field(...)
    user_id: str = Field(...)
    user_login: str = Field(...)
    user_name: str = Field(...)
    game_id: str = Field(...)
    game_name: str = Field(...)
    title: str = Field(...)

    @validator('id', pre=True)
    def validate_id(cls, v) -> str:
        return object_id_to_string(v)

    class Config:
        schema_extra = {
            'example': {
                'id': '62f264f7705d3742932262ec',
                'stream_id': '111',
                'user_id': '11111',
                'user_login': 'test_user_login',
                'user_name': 'test_user_name',
                'game_id': '100',
                'game_name': 'Resident Evil',
                'title': 'Best game',
            }
        }


class StreamsResponse(BaseModel):
    streams: List[Streams]


class StreamsUpdate(BaseModel):
    stream_id: Optional[str]
    user_id: Optional[str]
    user_login: Optional[str]
    user_name: Optional[str]
    game_id: Optional[str]
    game_name: Optional[str]
    title: Optional[str]

    class Config:
        schema_extra = {
            'example': {
                'stream_id': '111',
                'user_id': '11111',
                'user_login': 'test_user_login',
                'user_name': 'test_user_name',
                'game_id': '100',
                'game_name': 'Resident Evil',
                'title': 'Best game',
            }
        }
