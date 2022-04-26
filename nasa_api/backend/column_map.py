from nasa_api.flask_sql_table_schema import column_mapping

def get_column_map(study_id, page, per_page):
    results = column_mapping.query.filter_by(study_id=study_id).paginate(page=page, per_page=per_page)
    response = {}
    response["study_id"] = study_id
    data = []
    for result in results.items:
        data.append(
            {
                "genelab_column_name":result.column_name,
                "api_column_name":result.column_name_index
            }
        )
    meta = {
        'page':results.page,
        'pages':results.pages,
        'total_count':results.total,
        'prev_page':results.prev_num,
        'next_page':results.next_num,
        'has_next':results.has_next,
        'has_prev':results.has_prev
    }
    response['column_info'] = data
    response['meta'] = meta
    return response 