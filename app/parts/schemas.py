from pydantic import BaseModel, Field


class PartSchema(BaseModel):
    number: int = Field(
        title='Number of the part in Jojo',
        gt=0
    )
    name: str = Field(
        title='Name of part of Jojo'
    )
    japanese_name: str = Field(
        title='Name of part, but in japanese kanji'
    )
    alter_name: str | None = Field(
        default=None,
        title='This is the another o alternative names of Part'
    )

    class Config:
        orm_mode = True


class ListPartsSchema(BaseModel):
    data: list[PartSchema]

    class Config:
        orm_mode = True
