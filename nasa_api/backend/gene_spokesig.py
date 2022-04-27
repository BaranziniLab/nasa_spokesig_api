from nasa_api.flask_sql_table_schema import table_map, column_mapping
from nasa_api import flask_db

def get_gene_spokesig(study_id, col, page, per_page):
    table_name = '_'.join(study_id.split('-'))
    results = flask_db.session.query(getattr(table_map[table_name], col)).paginate(page=page, per_page=per_page)
    data = []
    for result in results.items:
        data.append(result[0])
    meta = {
        'page':results.page,
        'pages':results.pages,
        'total_count':results.total,
        'prev_page':results.prev_num,
        'next_page':results.next_num,
        'has_next':results.has_next,
        'has_prev':results.has_prev
    }
    results_2 = column_mapping.query.filter_by(study_id=study_id, column_name_index=col).all()
    response = {}
    response["study_id"] = study_id
    response["genelab_column_name"] = results_2[0].column_name
    response["api_column_name"] = col
    response["gene_spokesig"] = data
    response["meta"] = meta
    return response
    
    