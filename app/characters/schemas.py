from pydantic import BaseModel
from app.shared.schemas import PaginationSchema
from app.images.schemas import ImagesSchema


class CharacterSchema(BaseModel):
    name: str
    japanese_name: str
    alter_name: str | None = None
    images: ImagesSchema
    parts: list[int]
    is_human: bool = True
    living: bool = True
    is_ripple_user: bool = False
    is_stand_user: bool = False
    is_spin_user: bool = False
    catchphrase: str | None = None


class CharacterInDBSchema(CharacterSchema):
    id: int


class CharactersList(BaseModel):
    data: list[CharacterInDBSchema]
    pagination: PaginationSchema
