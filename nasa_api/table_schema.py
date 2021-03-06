from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
import pandas as pd
from nasa_api.config import read_config

c = dict(read_config().items('data'))
column_mapping_file = c['column_mapping_file']
Base = declarative_base()


class columnMapping(Base):
    __tablename__ = 'column_mapping'

    id = Column(Integer, primary_key=True, autoincrement=True)
    study_id = Column(String(15), nullable=False)
    column_name = Column(Text, nullable=False)
    column_name_index = Column(String(15), nullable=False)
    

class nodeMapping(Base):
    __tablename__ = 'node_mapping'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    Node = Column(String(20), nullable=False)
    Node_Name = Column(Text, nullable=False)
    Node_Type = Column(String(20), nullable=False)
    

'''
46 tables are needed, where each table corresponds to a study id. 
To automate the process of creation of these 46 tables, 
following section of the code creates Classes (that maps to study_id tables) 
in a dynamical fashion. Hence, this automates the creation of the 46 study_id tables. 
'''
column_mapping_df = pd.read_csv(column_mapping_file, sep='\t')
study_ids = list(column_mapping_df.study_id.unique())

var_holder = {}
for i in range(len(study_ids)):
    study_id_df = column_mapping_df[column_mapping_df.study_id == study_ids[i]]
    attribute_dict = {}
    table_name = '_'.join(study_ids[i].split('-'))
    attribute_dict['__tablename__'] = table_name
    attribute_dict['id'] = Column(Integer, primary_key=True, autoincrement=True)
    for index,row in study_id_df.iterrows():
        attribute_dict[row['column_name_index']] = Column(Integer, nullable=False)    
#     var_holder['studyID' + str(i+1)] = type('studyID' + str(i+1), (Base,), attribute_dict)
    var_holder[table_name] = type(table_name, (Base,), attribute_dict)

locals().update(var_holder)
    
    
    