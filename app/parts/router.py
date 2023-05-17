from typing import Annotated
from fastapi import APIRouter, status, Body, Path
from app.parts.schemas import ListPartsSchema, PartSchema
from app.parts.crud import PartRepositoryDep

router = APIRouter()


@router.get(
    '/parts',
    status_code=status.HTTP_200_OK,
    response_model=ListPartsSchema
)
async def get_parts(
    part_repository: PartRepositoryDep
):
    parts = part_repository.get_all()
    return parts


@router.get(
    '/parts/{number}',
    status_code=status.HTTP_200_OK,
    response_model=PartSchema
)
async def get_part(
        number: Annotated[int, Path()],
        part_repository: PartRepositoryDep
):
    part = part_repository.find_one(number)
    # return {**part.__dict__}
    return part


@router.post(
    '/parts',
    status_code=status.HTTP_201_CREATED,
    response_model=PartSchema
)
async def create_part(
    payload: Annotated[PartSchema | None, Body()],
    part_repository: PartRepositoryDep
):
    part = part_repository.create(payload)
    return part
