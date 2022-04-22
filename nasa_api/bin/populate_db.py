import pandas as pd
from nasa_api.config import read_config
from nasa_api.table_schema import columnMapping
from nasa_api import db
from sqlalchemy.orm import sessionmaker




A = [columnMapping(study_id=a.study_id, column_name=a.column_name, column_name_index=a.column_name_index) for a in df_.itertuples()]

Session = sessionmaker(db.engine())
session = Session()
session.add_all(A)
session.commit()