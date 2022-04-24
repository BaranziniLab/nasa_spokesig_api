"""
This script loads DB configs and provides access to table objects via sqlalchemy.
"""

from nasa_api.config import read_config
from urllib.parse import urlunparse
from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table



def db_url():
    c = dict(read_config().items('mysql'))
    scheme = 'mysql+pymysql'
    netloc = '{}:{}@{}:{}'.format(c['user'], c['password'],
                                  c['host'], c['port'])
    path = c['database']
    query = 'charset=utf8'
    return urlunparse((scheme, netloc, path, None, query, None))


@lru_cache()
def engine():
    return create_engine(db_url())


def begin():    
    return engine().begin()


def execute(*args, **kwargs):
    return engine().execute(*args, **kwargs)


@lru_cache()
def meta():
    return MetaData(bind=engine())


# class TableGetter(object):
#     def __getattr__(self, key):
#         if key in meta().tables:
#             return meta().tables[key]
#         return Table(key, meta(), autoload=True)
    
#     def __getitem__(self, key):
#         if key in meta().tables:
#             return meta().tables[key]
#         return Table(key, meta(), autoload=True)
    
# # Now, tables can be accessed as T.<table name>
# T = TableGetter()

