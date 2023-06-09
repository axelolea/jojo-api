from typing import Annotated

from fastapi import Depends, HTTPException

from app.db.repository import BaseRepository, get_repository

from app.characters.model import Character
from app.characters.schemas import CharacterSchema

from app.images.model import Images


class CharacterRepository(BaseRepository):

    def create(self, payload: CharacterSchema) -> Character:
        new_character = Character(**payload.dict())
        new_images = Images(**payload.images.dict())
        new_character.images_id = new_images.id

        self.db.add(new_character)
        self.db.add(new_images)
        self.db.commit()
        self.db.refresh(new_character)
        self.db.refresh(new_images)
        return new_character

    def find_one(self, character_id: int) -> Character | None:
        return self.db.query(Character).filter_by(id=character_id).first()

    def get_all(self) -> list[type[Character]]:
        return self.db.query(Character).all()


CharacterRepositoryDep = Annotated[CharacterRepository, Depends(get_repository(CharacterRepository))]
