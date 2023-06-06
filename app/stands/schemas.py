from pydantic import BaseModel

from app.images.schemas import ImagesSchema
from app.shared.schemas import PaginationSchema

from app.utils.constants import StatsEnum


class StatsSchema(BaseModel):
    power: StatsEnum
    speed: StatsEnum
    range: StatsEnum
    durability: StatsEnum
    precision: StatsEnum
    potential: StatsEnum


class StandSchema(BaseModel):
    name: str
    japanese_name: str
    alter_name: str | None = None
    images: ImagesSchema
    parts: list
    abilities: str
    battlecry: str | None = None
    stats: StatsSchema


class StandInDBSchema(StandSchema):
    id: int


class StandsList(BaseModel):
    data: list[StandInDBSchema]
    pagination: PaginationSchema
