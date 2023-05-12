from pydantic import BaseModel


class PartSchema(BaseModel):
    number: int
    name: str
    japanese_name: str
    alter_name: str | None = None


class ListPartsSchema(BaseModel):
    data: list[PartSchema]
