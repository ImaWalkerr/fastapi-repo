from typing import Optional, List
from pydantic import BaseModel, Field, validator
from src.models.validators.object_id import object_id_to_string


class Clothes(BaseModel):
    id: str = Field(..., alias="_id")
    name: str = Field(...)
    brand: str = Field(...)
    price: str = Field(...)

    @validator('id', pre=True)
    def validate_id(cls, v) -> str:
        return object_id_to_string(v)

    class Config:
        schema_extra = {
            'example': {
                'id': '62f264f7705d3742932262ec',
                'name': 'Singlet',
                'brand': 'Miguel de Cervantes',
                'price': '399.00'
            }
        }


class ClothesResponse(BaseModel):
    clothes: List[Clothes]


class ClothesUpdate(BaseModel):
    name: Optional[str]
    brand: Optional[str]
    price: Optional[str]

    class Config:
        schema_extra = {
            'example': {
                'name': 'Singlet',
                'brand': 'Miguel de Cervantes',
                'price': '399.00'
            }
        }
