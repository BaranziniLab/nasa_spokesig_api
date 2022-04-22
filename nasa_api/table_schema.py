from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text


Base = declarative_base()


class columnMapping(Base):
    __tablename__ = 'column_mapping'

    id = Column(Integer, primary_key=True, autoincrement=True)
    study_id = Column(String(15), nullable=False)
    column_name = Column(Text, nullable=False)
    column_name_index = Column(String(15), nullable=False)
