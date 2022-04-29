from nasa_api.flask_sql_table_schema import node_mapping

def get_node_map(page, per_page):
    results = node_mapping.query.paginate(page=page, per_page=per_page)
    response = {}
    data = []
    for result in results.items:
        data.append(            
            {                
                "node_id":result.Node,
                "node_name":result.Node_Name,
                "node_type":result.Node_Type,
                "spokesig_index":result.id-1
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
    response["node"] = data
    response["meta"] = meta
    return response 
        
        
    