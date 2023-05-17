from typing import Annotated

from fastapi import Depends
# from fastapi.encoders import jsonable_encoder

from app.db.repository import BaseRepository, get_repository

from app.parts.model import Part
from app.parts.schemas import PartSchema


class PartRepository(BaseRepository):

    def create(self, payload: PartSchema) -> Part:
        new_part = Part(**payload.dict())
        self.db.add(new_part)
        self.db.commit()
        self.db.refresh(new_part)
        return new_part

    def find_one(self, part_number: int) -> Part | None:
        return self.db.query(Part).filter_by(number=part_number).first()

    def get_all(self) -> list[type[Part]]:
        return self.db.query(Part).all()


PartRepositoryDep = Annotated[PartRepository, Depends(get_repository(PartRepository))]
