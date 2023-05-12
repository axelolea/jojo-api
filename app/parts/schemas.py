from pydantic import BaseModel


class PartSchema(BaseModel):
    number: int
    name: str


class PartInDBSchema(PartSchema):
    japanese_name: str
    alter_name: str


class ListPartsSchema(BaseModel):
    data: list[PartSchema]
