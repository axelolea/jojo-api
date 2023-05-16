from sqlalchemy import String, Integer, Column
from app.db.config import Base
from sqlalchemy.orm import relationship


class Part(Base):
    __tablename__ = 'parts'
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=False, index=True)
    name = Column(String, nullable=False)
    japanese_name = Column(String)
    alter_name = Column(String)

    stands = relationship('Stand', back_populates='parts')
    # characters = relationship('Stand', back_populates='parts')
