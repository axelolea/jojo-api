from sqlalchemy import String, Integer, Column
from app.db.config import Base
# from sqlalchemy.orm import relationship


class Part(Base):

    __tablename__ = 'parts'

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=False)
    name = Column(String(length=50), nullable=False)
    japanese_name = Column(String(length=50))
    alter_name = Column(String(length=100))

    def __str__(self) -> str:
        return f'<< {self.number} .- {self.name} >>'

    # stands = relationship('Stand', back_populates='parts')
    # characters = relationship('Stand', back_populates='parts')
