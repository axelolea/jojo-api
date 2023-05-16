from sqlalchemy import String, Column
from app.db.config import Base
from sqlalchemy.orm import relationship


class Stand(Base):

    __tablename__ = 'stands'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    japanese_name = Column(String, nullable=False)
    alter_name = Column(String)
    battlecry = Column(String)
    abilities = Column(String, nullable=False)
    # images: ImagesSchema
    # stats: StatsSchema

    parts = relationship('Parts', back_populates='stands')
