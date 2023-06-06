from sqlalchemy import String, Integer, Column
from app.db.config import Base
from sqlalchemy.orm import relationship


class Images(Base):

    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, index=True)
    half_body = Column(String(length=200), nullable=False)
    full_body = Column(String(length=200))

    def __str__(self) -> str:
        return f'<< Image({self.half_body}, {self.full_body}) >>'

    # Many to many
    stands = relationship('Stand', uselist=False, back_populates='images')
    characters = relationship('Character', uselist=False, back_populates='images')
