from fastapi import APIRouter, status, Body
from typing import Annotated
from app.characters.schemas import (
    CharacterInDBSchema,
    CharactersList,
    CharacterSchema
)

router = APIRouter()


@router.get(
    '',
    status_code=status.HTTP_200_OK,
    response_model=CharactersList
)
def get_characters():

    ...


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=CharacterInDBSchema
)
def get_characters(
    payload: Annotated[CharacterSchema, Body()]
):

    ...


@router.get(
    '/{number}'
)
def get_characters(number: int):

    ...
