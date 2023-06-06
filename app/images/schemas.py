from pydantic import BaseModel


class ImagesSchema(BaseModel):
    full_body: str | None = None
    half_body: str


class ImagesInDBSchema(ImagesSchema):
    id: int


class ImagesList(BaseModel):
    data: list[ImagesSchema]
