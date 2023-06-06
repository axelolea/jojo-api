from fastapi import APIRouter

from app.images.schemas import ImagesSchema

router = APIRouter()


@router.get(
    '/{number}',
    status_code=200,
    response_model=ImagesSchema
)
def get_image_with_id(number: int):

    ...
