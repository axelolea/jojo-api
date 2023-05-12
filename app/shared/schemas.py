from pydantic import BaseModel


class PaginationSchema(BaseModel):
    page: int
    per_page: int
    total: int
    previous: bool
    next: bool


class ImagesSchema(BaseModel):
    full_body: str | None = None
    half_body: str
