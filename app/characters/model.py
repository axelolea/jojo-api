from sqlalchemy import String, Column, Integer, Boolean, ForeignKey
from app.db.config import Base
from sqlalchemy.orm import relationship


class Character(Base):

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=120), nullable=False)
    japanese_name = Column(String(length=120), nullable=False)
    images_id = Column(Integer, ForeignKey('images.id'))
    alter_name = Column(String(length=120))
    is_human = Column(Boolean, default=True)
    living = Column(Boolean, default=True)
    is_ripple_user = Column(Boolean, default=False)
    is_stand_user = Column(Boolean, default=False)
    is_spin_user = Column(Boolean, default=False)
    catchphrase = Column(String(length=200))

    images = relationship('Images', back_populates='characters')
    parts = relationship('Part', back_populates='characters')
