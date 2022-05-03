from unittest.mock import patch
from tests.case import FlaskTestCase
import nasa_api
from nasa_api import *



class HomeAPITestCase(FlaskTestCase):
    
    def test_valid_api_call(self):
        resp = self.client.get(
            "/nasa_api"
        )
        
        self.assertEqual(
            resp.status_code, 
            200
        )
        
        self.assertEqual(
            resp.json,
            dict(
                api_name=APP_NAME,
                version=nasa_api.__version__
            )
        )
        

                
class ColumnMapAPITestCase(FlaskTestCase):
    
    def setUp(self):
        super().setUp()
        
        self.get_column_map = self.start(
            patch('nasa_api.app.get_column_map', return_value=
                  dict(
                     study_id="GLDS-47",
                     column_info=[
                         dict(
                             genelab_column_name="Log2fc_(BASAL)v(Space Flight)",
                             api_column_name="col1"
                         ),
                         dict(
                             genelab_column_name="Log2fc_(BASAL)v(Ground Control)",
                             api_column_name="col2"
                         ),
                         dict(
                             genelab_column_name="Log2fc_(Space Flight)v(Ground Control)",
                             api_column_name="col3"
                         ),
                         dict(
                             genelab_column_name="Log2fc_(Space Flight)v(BASAL)",
                             api_column_name="col4"
                         ),
                         dict(
                             genelab_column_name="Log2fc_(Ground Control)v(BASAL)",
                             api_column_name="col5"
                         )
                     ],
                     meta=dict(
                         page=1,
                         pages=2,
                         total_count=6,
                         prev_page="null",
                         next_page=2,
                         has_next="true",
                         has_prev="false"
                     )
                 )
                )
        )
        
    
    def test_valid_api_call(self):
        resp = self.client.get(
            "/nasa_api/v1/column_map",
            query_string=dict(
                study_id="GLDS-47",
                page=1,
                per_page=5
            )
        )
        
        self.assertEqual(
            resp.status_code, 
            200
        )
        
        self.assertEqual(resp.json,
                         dict(
                             study_id="GLDS-47",
                             column_info=[
                                 dict(
                                     genelab_column_name="Log2fc_(BASAL)v(Space Flight)",
                                     api_column_name="col1"
                                 ),
                                 dict(
                                     genelab_column_name="Log2fc_(BASAL)v(Ground Control)",
                                     api_column_name="col2"
                                 ),
                                 dict(
                                     genelab_column_name="Log2fc_(Space Flight)v(Ground Control)",
                                     api_column_name="col3"
                                 ),
                                 dict(
                                     genelab_column_name="Log2fc_(Space Flight)v(BASAL)",
                                     api_column_name="col4"
                                 ),
                                 dict(
                                     genelab_column_name="Log2fc_(Ground Control)v(BASAL)",
                                     api_column_name="col5"
                                 )
                             ],
                             meta=dict(
                                 page=1,
                                 pages=2,
                                 total_count=6,
                                 prev_page="null",
                                 next_page=2,
                                 has_next="true",
                                 has_prev="false"
                             )
                         )
                        )
        
        self.get_column_map.assert_called_once_with(
            study_id="GLDS-47",
            page=1,
            per_page=5
        )
        
    def test_incorrect_format_study_id(self):
        resp = self.client.get(
            "/nasa_api/v1/column_map",
            query_string=dict(
                study_id="GLDS_47",
                page=1,
                per_page=5
            )
        )
        
        self.assertEqual(
            resp.status_code,
            422
        )
        
        self.assertEqual(
            resp.json,
            dict(
                message="study_id is not given in the correct format.",
                status_code=422,
                details= "study_id starts with 'GLDS-'"
            )
        )
        
    def test_invalid_study_id(self):
        resp = self.client.get(
            "/nasa_api/v1/column_map",
            query_string=dict(
                study_id="GLDS-11",
                page=1,
                per_page=5
            )
        )
        
        self.assertEqual(
            resp.status_code,
            422
        )
        
        self.assertEqual(
            resp.json,
            dict(
                message="Given study_id is invalid",
                status_code=422
            )
        )
        
        
        
        
class GeneSpokesigAPITestCase(FlaskTestCase):
    
    def setUp(self):
        super().setUp()
        self.get_gene_spokesig = self.start(
            patch('nasa_api.app.get_gene_spokesig', return_value=
                  dict(
                      study_id="GLDS-47",
                      genelab_column_name="Log2fc_(BASAL)v(Space Flight)",
                      api_column_name="col1",
                      gene_spokesig=[
                          1135,
                          3898,
                          4070,
                          3261,
                          8206                      
                      ],
                      meta=dict(
                         page=1,
                         pages=77860,
                         total_count=389297,
                         prev_page="null",
                         next_page=2,
                         has_next="true",
                         has_prev="false"
                      )
                  )
             )
        )
        
    def test_valid_api_call(self):
        resp = self.client.get(
            "/nasa_api/v1/gene_spokesig",
            query_string=dict(
                study_id="GLDS-47",
                col="col1",
                page=1,
                per_page=5
            )
        )
        
        self.assertEqual(
            resp.status_code, 
            200
        )
        
        self.assertEqual(
            resp.json,
            dict(
                  study_id="GLDS-47",
                  genelab_column_name="Log2fc_(BASAL)v(Space Flight)",
                  api_column_name="col1",
                  gene_spokesig=[
                      1135,
                      3898,
                      4070,
                      3261,
                      8206                      
                  ],
                  meta=dict(
                     page=1,
                     pages=77860,
                     total_count=389297,
                     prev_page="null",
                     next_page=2,
                     has_next="true",
                     has_prev="false"
                  )
            )
        )
        
        self.get_gene_spokesig.assert_called_once_with(
            study_id="GLDS-47",
            col="col1",
            page=1,
            per_page=5
        )
        
    def test_incorrect_format_study_id(self):
        resp = self.client.get(
            "/nasa_api/v1/gene_spokesig",
            query_string=dict(
                study_id="GLDS_47",
                col="col1",
                page=1,
                per_page=5
            )
        )
        
        self.assertEqual(
            resp.status_code,
            422
        )
        
        self.assertEqual(
            resp.json,
            dict(
                message="study_id is not given in the correct format.",
                status_code=422,
                details= "study_id starts with 'GLDS-'"
            )
        )
        
    def test_invalid_study_id(self):
        resp = self.client.get(
            "/nasa_api/v1/gene_spokesig",
            query_string=dict(
                study_id="GLDS-11",
                col="col1",
                page=1,
                per_page=5
            )
        )
        
        self.assertEqual(
            resp.status_code,
            422
        )
        
        self.assertEqual(
            resp.json,
            dict(
                message="Given study_id is invalid",
                status_code=422
            )
        )
        
    def test_invalid_col(self):
        resp = self.client.get(
            "/nasa_api/v1/gene_spokesig",
            query_string=dict(
                study_id="GLDS-47",
                col="col100",
                page=1,
                per_page=5
            )
        )
        
        self.assertEqual(
            resp.status_code,
            422
        )
        
        self.assertEqual(
            resp.json,
            dict(
                message="Given column is invalid for the study_id GLDS-47",
                status_code=422,
                details= "There are only 6 columns for this study_id"
            )
        )
        
        
            
class NodeMapAPITestCase(FlaskTestCase):
    
    def setUp(self):
        super().setUp()
        
        self.get_node_map = self.start(
            patch('nasa_api.app.get_node_map', return_value=
                  dict(
                      node=[
                          dict(
                              node_id="1",
                              node_name="A1BG",
                              node_type="Gene",
                              spokesig_index=0
                          )
                      ],
                      meta=dict(
                          page=1,
                          pages=389297,
                          total_count=389297,
                          prev_page="null",
                          next_page= 2,
                          has_next= "true",
                          has_prev="false"
                      )
                  )
                 )
        )
        
    def test_valid_api_call(self):
        resp = self.client.get(
            "/nasa_api/v1/node_map",
            query_string=dict(
                page=1,
                per_page=1
            )
        )
        
        self.assertEqual(
            resp.status_code, 
            200
        )
        
        self.assertEqual(
            resp.json,
            dict(
                  node=[
                      dict(
                          node_id="1",
                          node_name="A1BG",
                          node_type="Gene",
                          spokesig_index=0
                      )
                  ],
                  meta=dict(
                      page=1,
                      pages=389297,
                      total_count=389297,
                      prev_page="null",
                      next_page= 2,
                      has_next= "true",
                      has_prev="false"
                  )
              )
        )
     