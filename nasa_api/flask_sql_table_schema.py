from nasa_api import flask_db
import pandas as pd
from nasa_api.config import read_config

c = dict(read_config().items('data'))
column_mapping_file = c['column_mapping_file']

class column_mapping(flask_db.Model):
    id = flask_db.Column(flask_db.Integer, primary_key=True, autoincrement=True)
    study_id = flask_db.Column(flask_db.String(15), nullable=False)
    column_name = flask_db.Column(flask_db.Text, nullable=False)
    column_name_index = flask_db.Column(flask_db.String(15), nullable=False)
    
    
class node_mapping(flask_db.Model):
    id = flask_db.Column(flask_db.Integer, primary_key=True, autoincrement=True)
    Node = flask_db.Column(flask_db.String(20), nullable=False)
    Node_Name = flask_db.Column(flask_db.Text, nullable=False)
    Node_Type = flask_db.Column(flask_db.String(20), nullable=False)
    
            
column_mapping_df = pd.read_csv(column_mapping_file, sep='\t')
study_ids = list(column_mapping_df.study_id.unique())

table_map = {}
for i in range(len(study_ids)):
    study_id_df = column_mapping_df[column_mapping_df.study_id == study_ids[i]]
    attribute_dict = {}
    table_name = '_'.join(study_ids[i].split('-'))
    attribute_dict['id'] = flask_db.Column(flask_db.Integer, primary_key=True, autoincrement=True)
    for index,row in study_id_df.iterrows():
        attribute_dict[row['column_name_index']] = flask_db.Column(flask_db.Integer, nullable=False)    
    table_map[table_name] = type(table_name, (flask_db.Model,), attribute_dict)

locals().update(table_map)

    