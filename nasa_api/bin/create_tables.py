from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
from nasa_api import db
from sqlalchemy_utils import create_database, database_exists


       
print('Checking if database exists ...')
if not database_exists(db.db_url()):
    print('Database does not exist, creating it now ...')
    create_database(db.db_url())
    print('Database is created!')
else:
    print('Database already exists.')

                
Base = declarative_base()

print('Creating column_mapping table ...')
class columnMapping(Base):
    __tablename__ = 'column_mapping'

    id = Column(Integer, primary_key=True, autoincrement=True)
    study_id = Column(String(15), nullable=False)
    column_name = Column(Text, nullable=False)
    column_name_index = Column(String(15), nullable=False) 

Base.metadata.create_all(db.engine(), checkfirst=True)
print('column_mapping table is created!')
    
    