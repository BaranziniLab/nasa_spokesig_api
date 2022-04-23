import pandas as pd
import numpy as np
import os
import itertools
from nasa_api.config import read_config
from tqdm import tqdm


c = dict(read_config().items('data'))
gene_spokesig_path = c['gene_spokesig_path']
column_mapping_file = c['column_mapping_file']

def main():
    if not os.path.exists(column_mapping_file):
        print('Column mapping file does not exist. Creating it now ...')
        study_files = list(filter(None, list(map(lambda x:x if '.tsv' in x else None, os.listdir(gene_spokesig_path)))))
        study_ids = list(filter(None, list(map(lambda x:x.split('_rank_by_type')[0], study_files))))
        print('Parsing columns of each study file ...')
        study_id_with_columns_list = []
        for study_file in tqdm(study_files):
            study_id = study_file.split('_rank_by_type')[0]
            df = pd.read_csv(os.path.join(gene_spokesig_path, study_file), sep='\t')
            columns = list(df.columns)
            sel_columns = list(filter(None, list(map(lambda x:x if 'Rank_by_type' in x else None, columns))))
            study_id_with_columns_list.append(list(zip([study_id]*len(sel_columns), sel_columns, list(np.arange(len(sel_columns))+1))))

        study_id_with_columns_list_ = list(itertools.chain(*study_id_with_columns_list))
        study_id_with_columns_df = pd.DataFrame(study_id_with_columns_list_, columns = ['study_id', 'column_name', 'column_name_index'])
        study_id_with_columns_df.column_name = study_id_with_columns_df.column_name.apply(lambda x:x.split('Rank_by_type_')[-1])
        study_id_with_columns_df.column_name_index = study_id_with_columns_df.column_name_index.astype('str')
        study_id_with_columns_df.column_name_index =  'col'+study_id_with_columns_df.column_name_index
        print('Saving column mapping file ...')
        study_id_with_columns_df.to_csv(column_mapping_file, sep='\t', index=False, header=True)
        print('Saved!')
    else:
        print('Column mapping file already exists.')

if __name__ == "__main__":
    main()