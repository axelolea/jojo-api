from pydantic import BaseModel
from enum import Enum
from app.shared.schemas import ImagesSchema

stats_values = Enum(
    'StatsValues',
    ['NULL', 'A', 'B', 'C', 'D', 'E', 'INFINITE', '?']
)


class StatsSchema(BaseModel):
    power: stats_values
    speed: stats_values
    range: stats_values
    durability: stats_values
    precision: stats_values
    potential: stats_values


class Stand(BaseModel):
    id: int
    name: str
    japanese_name: str
    alter_name: str | None = None
    abilities: str
    battlecry: str | None = None
    images: ImagesSchema
    stats: StatsSchema
