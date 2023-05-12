from fastapi import APIRouter, HTTPException, status
from app.parts.schemas import ListPartsSchema

router = APIRouter()


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model=ListPartsSchema
)
async def get_parts():

    return []
