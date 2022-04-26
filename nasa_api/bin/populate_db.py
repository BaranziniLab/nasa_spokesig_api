from nasa_api.table_schema import *
from nasa_api import db
from nasa_api.db import Table
from nasa_api.bin.create_column_mappings import get_gene_spokesig_study_files, gene_spokesig_path
import numpy as np
import os



def main():
    global study_files
    
    print('Populating {} table ...'.format(columnMapping.__tablename__))
    fill_table(Table(columnMapping.__tablename__, db.meta(), autoload=True), column_mapping_df.to_dict(orient='records'))
    print('Populated {} table!'.format(columnMapping.__tablename__))
    print(' ')
    
    print('Populating {} table ...'.format(nodeMapping.__tablename__))
    node_mapping_data_df = get_node_mapping_data()
    fill_table(Table(nodeMapping.__tablename__, db.meta(), autoload=True), node_mapping_data_df.to_dict(orient='records'))
    print('Populated {} table!'.format(nodeMapping.__tablename__))
    print(' ')
    
    study_files = get_gene_spokesig_study_files()
    for index, study_id in enumerate(study_ids):    
        study_id_data_to_populate_df = get_study_id_data_to_populate(study_id)
        table_name = '_'.join(study_id.split('-'))
        print('Populating table : {} ({}/{}) ...'.format(table_name, index+1, len(study_ids)))
        fill_table(Table(table_name, db.meta(), autoload=True), study_id_data_to_populate_df.to_dict(orient='records'))
        print('Populated table {} ({}/{})!'.format(table_name, index+1, len(study_ids)))
        print(' ')


def get_node_mapping_data():
    node_mapping_data_df = pd.read_csv(os.path.join(gene_spokesig_path, 'GLDS-87_rank_by_type_0_1.tsv'), sep='\t')
    return node_mapping_data_df[['Node', 'Node_Name', 'Node_Type']]

        
def get_study_id_data_to_populate(study_id):
    selected_study_file = study_files[np.where(list(map(lambda x:study_id == x.split('_')[0] in x, study_files)))[0][0]]
    print('Reading data of study id : {}'.format(study_id))
    study_id_df = pd.read_csv(os.path.join(gene_spokesig_path, selected_study_file), sep='\t')
    columns = list(study_id_df.columns)
    sel_columns = list(filter(None, list(map(lambda x:x if 'Rank_by_type' in x else None, columns))))
    study_id_df_ = study_id_df[sel_columns]
    study_id_column_df = column_mapping_df[column_mapping_df.study_id==study_id]
    new_column_names = list(study_id_column_df['column_name_index'])
    study_id_df_.columns = new_column_names
    study_id_df_ = study_id_df_.astype('int')
    return study_id_df_
    

def fill_table(table, rows):
    with db.begin() as trans:
        trans.execute(table.delete())
        if rows:
            trans.execute(table.insert(), rows)

            
if __name__ == "__main__":
    main()