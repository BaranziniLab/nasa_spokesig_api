from webargs.flaskparser import use_kwargs
from webargs.fields import Str, Int
from webargs import validate
import nasa_api
from nasa_api import *
from nasa_api.config import read_config
from nasa_api.table_schema import study_ids
from nasa_api.flask_sql_table_schema import column_mapping
from nasa_api.backend.column_map import get_column_map
from nasa_api.backend.gene_spokesig import get_gene_spokesig 
from nasa_api.backend.node_map import get_node_map


@app.route('/nasa_api', methods=['GET'])
def home():
#     endpoints = sorted(r.rule for r in app.url_map.iter_rules())
    return jsonify(
        api_name=APP_NAME,
        version=nasa_api.__version__
    )

@app.route("/nasa_api/v1/column_map", methods=['GET'])
@use_kwargs(
    dict(
        study_id=Str(
                    data_key="study_id",
                    required=True                    
        ),
        page=Int(
                    data_key="page"
        ),
        per_page=Int(
                    data_key="per_page"
        )
    ),
    location="query"
)
def column_map(study_id, page=1, per_page=10):
    if not "GLDS-" in study_id:
        return problem_response(
            message="study_id is not given in the correct format.", 
            details = "study_id starts with 'GLDS-'"            
        )
    if not study_id in study_ids:
        return problem_response(
            message="Given study_id is invalid"
        )

    return jsonify(
        get_column_map(            
            study_id=study_id,
            page=page,
            per_page=per_page
        )
    )
                    
    
@app.route("/nasa_api/v1/gene_spokesig", methods=['GET'])
@use_kwargs(
    dict(
        study_id=Str(
            data_key="study_id",
            required=True 
        ),
        col=Str(
            data_key="col",
            required=True
        ),
        page=Int(
            data_key="page"
        ),
        per_page=Int(
            data_key="per_page"
        )
    ),
    location="query"
)
def gene_spokesig(study_id, col, page=1, per_page=100):
    if not "GLDS-" in study_id:
        return problem_response(
            message="study_id is not given in the correct format.",
            details = "study_id starts with 'GLDS-'"
        )         
    if not study_id in study_ids:
        return problem_response(
            message="Given study_id is invalid"
        )
    col_list = get_columns(study_id)
    if not col in col_list:
        return problem_response(
            message="Given column is invalid for the study_id %s"%study_id,
            details="There are only %d columns for this study_id"%len(col_list)
        )        
    
    return jsonify(
        get_gene_spokesig(
            study_id=study_id,
            col=col,
            page=page,
            per_page=per_page
        )
    )
        

@app.route("/nasa_api/v1/node_map", methods=['GET'])
@use_kwargs(
    dict(        
        page=Int(
            data_key="page"
        ),
        per_page=Int(
            data_key="per_page"
            )
    ),
    location="query"
)
def node_map(page=1, per_page=100): 
    return jsonify(
        get_node_map(
            page=page,
            per_page=per_page
        )
    )
        

    
def get_columns(study_id):
    column_results = column_mapping.query.filter_by(study_id=study_id).all()
    col_list = []
    for item in column_results:
        col_list.append(item.column_name_index)
    return col_list
    
        
if __name__=="__main__":
    app.run(**dict(read_config().items('flask')))
        

                    
   
        