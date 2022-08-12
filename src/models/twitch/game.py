from typing import Optional, List
from pydantic import BaseModel, Field, validator
from src.models.validators.object_id import object_id_to_string


class Games(BaseModel):
    id: str = Field(..., alias="_id")
    game_id: str = Field(...)
    name: str = Field(...)
    summary: str = Field(...)
    genres: str = Field(...)
    platforms: str = Field(...)
    release_dates: str = Field(...)
    rating: str = Field(...)
    rating_count: str = Field(...)
    cover_url: str = Field(...)
    screenshot_url: str = Field(...)

    @validator('id', pre=True)
    def validate_id(cls, v) -> str:
        return object_id_to_string(v)

    class Config:
        schema_extra = {
            'example': {
                'id': '62f264f7705d3742932262ec',
                'game_id': '100',
                'name': 'Resident Evil',
                'summary': 'The best horror game',
                'genres': 'Horror',
                'platforms': 'Win',
                'release_dates': '1998, 2021',
                'rating': '98',
                'rating_count': '19',
                'cover_url': 'test_url',
                'screenshot_url': 'test_url'
            }
        }


class GamesResponse(BaseModel):
    games: List[Games]


class GamesUpdate(BaseModel):
    game_id: Optional[str]
    name: Optional[str]
    summary: Optional[str]
    genres: Optional[str]
    platforms: Optional[str]
    release_dates: Optional[str]
    rating: Optional[str]
    rating_count: Optional[str]
    cover_url: Optional[str]
    screenshot_url: Optional[str]

    class Config:
        schema_extra = {
            'example': {
                'game_id': '100',
                'name': 'Resident Evil',
                'summary': 'The best horror game',
                'genres': 'Horror',
                'platforms': 'Win',
                'release_dates': '1998, 2021',
                'rating': '98',
                'rating_count': '19',
                'cover_url': 'test_url',
                'screenshot_url': 'test_url'
            }
        }
