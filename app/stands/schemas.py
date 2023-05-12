from pydantic import BaseModel
from enum import Enum

from app.images.schemas import ImagesSchema
from app.shared.schemas import PaginationSchema

StatsValues = Enum(
    'StatsValues',
    ['NULL', 'A', 'B', 'C', 'D', 'E', 'INFINITE', '?']
)


class StatsSchema(BaseModel):
    power: StatsValues
    speed: StatsValues
    range: StatsValues
    durability: StatsValues
    precision: StatsValues
    potential: StatsValues


class StandSchema(BaseModel):
    name: str
    japanese_name: str
    alter_name: str | None = None
    images: ImagesSchema
    parts: list
    abilities: str
    battlecry: str | None = None
    stats: StatsSchema


class StandInDB(StandSchema):
    id: int


class StandsList(BaseModel):
    data: list[StandInDB]
    pagination: PaginationSchema
