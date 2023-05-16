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
async def get_parts():

    return []


@router.get(
    '/parts/{number}',
    status_code=status.HTTP_200_OK,
    response_model=PartSchema
)
async def get_part(number: Annotated[int, Path()]):

    return {}


@router.post(
    '/parts',
    status_code=status.HTTP_201_CREATED,
    response_model=PartSchema
)
async def create_part(
    payload: Annotated[PartSchema, Body()],
    part_repository: PartRepositoryDep
):
    part = part_repository.create(payload)
    return part
