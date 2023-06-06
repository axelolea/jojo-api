from sqlalchemy import String, Column, Integer, ForeignKey
from app.db.config import Base
from sqlalchemy.orm import relationship


class Stand(Base):

    __tablename__ = 'stands'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=120), nullable=False)
    japanese_name = Column(String(length=120), nullable=False)
    alter_name = Column(String(length=120))
    battlecry = Column(String(length=200))
    abilities = Column(String(length=200), nullable=False)
    images_id = Column(Integer, ForeignKey('images.id'))
    stats_id = Column(Integer, ForeignKey('stats.id'))

    # Many to many
    parts = relationship('Parts', back_populates='stands')

    # One to one
    images = relationship('Images', back_populates='stands')
    stats = relationship('Stats', back_populates='stands')


class Stats(Base):

    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True, index=True)
    power = Column(String(length=8), nullable=False)
    speed = Column(String(length=8), nullable=False)
    range = Column(String(length=8), nullable=False)
    durability = Column(String(length=8), nullable=False)
    precision = Column(String(length=8), nullable=False)
    potential = Column(String(length=8), nullable=False)

    # One to one
    stand = relationship('Stand', uselist=False, back_populates='stand')
