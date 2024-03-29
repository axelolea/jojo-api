from typing import Annotated
from fastapi import APIRouter, status, Body, Path, HTTPException
from app.parts.schemas import ListPartsSchema, PartSchema
from app.parts.crud import PartRepositoryDep

router = APIRouter()


@router.get(
    '',
    status_code=status.HTTP_200_OK,
    response_model=ListPartsSchema
)
async def get_parts(
    part_repository: PartRepositoryDep
):
    parts = part_repository.get_all()
    return {'data': parts}


@router.get(
    '/{number}',
    status_code=status.HTTP_200_OK,
    response_model=PartSchema
)
async def get_part_with_number(
        number: Annotated[int, Path()],
        part_repository: PartRepositoryDep
):
    part = part_repository.find_one(number)
    if not part:
        raise HTTPException(
            status_code=404,
        )
    return part


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=PartSchema
)
async def create_part(
    payload: Annotated[PartSchema, Body()],
    part_repository: PartRepositoryDep
):
    part = part_repository.create(payload)
    return part
