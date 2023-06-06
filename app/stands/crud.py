from typing import Annotated

from fastapi import Depends, HTTPException

from app.db.repository import BaseRepository, get_repository

from app.stands.models import Stand, Stats
from app.stands.schemas import StandSchema, StatsSchema


class StandRepository(BaseRepository):

    def create(self, payload: StandSchema) -> Stand:
        new_part = Stand(**payload.dict())

        stands = self.db.query(Stand).filter_by().first()


        self.db.add(new_part)
        self.db.commit()
        self.db.refresh(new_part)
        return new_part

    def find_one(self, part_number: int) -> Stand | None:
        return self.db.query(Stand).filter_by(number=part_number).first()

    def get_all(self) -> list[type[Stand]]:
        return self.db.query(Stand).all()


StandRepositoryDep = Annotated[StandRepository, Depends(get_repository(StandRepository))]
