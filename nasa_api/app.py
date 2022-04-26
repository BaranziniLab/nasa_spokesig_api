from flask import make_response
from flask import jsonify
from webargs.flaskparser import use_kwargs
from webargs.fields import Str, Int
from webargs import validate
from nasa_api import *
from nasa_api.config import read_config
from nasa_api.backend.column_map import get_column_map



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
        return make_response("Bad request. study_id is not given in the correct format. study_id starts with 'GLDS-'", 400)
    return jsonify(
        get_column_map(            
            study_id=study_id,
            page=page,
            per_page=per_page
        )
    )
                    
        
        
if __name__=="__main__":
        app.run(**dict(read_config().items('flask')))
        

                    
   
        