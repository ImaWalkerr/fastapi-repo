from typing import Optional, List
from pydantic import BaseModel, Field, validator
from src.models.validators.object_id import object_id_to_string


class Streamers(BaseModel):
    id: str = Field(..., alias="_id")
    stream_id: str = Field(...)
    game_id: str = Field(...)
    game_name: str = Field(...)
    viewer_count: str = Field(...)
    started_at: str = Field(...)
    language: str = Field(...)
    tags_id: str = Field(...)
    is_mature: str = Field(...)

    @validator('id', pre=True)
    def validate_id(cls, v) -> str:
        return object_id_to_string(v)

    class Config:
        schema_extra = {
            'example': {
                'id': '62f264f7705d3742932262ec',
                'stream_id': '111',
                'game_id': '100',
                'game_name': 'Resident Evil',
                'viewer_count': '123113',
                'started_at': '2022',
                'language': 'en',
                'tags_id': '132123',
                'is_mature': 'true'
            }
        }


class StreamersResponse(BaseModel):
    streamers: List[Streamers]


class StreamersUpdate(BaseModel):
    stream_id: Optional[str]
    game_id: Optional[str]
    game_name: Optional[str]
    viewer_count: Optional[str]
    started_at: Optional[str]
    language: Optional[str]
    tags_id: Optional[str]
    is_mature: Optional[str]

    class Config:
        schema_extra = {
            'example': {
                'stream_id': '111',
                'game_id': '100',
                'game_name': 'Resident Evil',
                'viewer_count': '123113',
                'started_at': '2022',
                'language': 'en',
                'tags_id': '132123',
                'is_mature': 'true'
            }
        }
