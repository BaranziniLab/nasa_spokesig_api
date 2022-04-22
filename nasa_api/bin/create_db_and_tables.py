from nasa_api import db
from nasa_api.table_schema import Base
from sqlalchemy_utils import create_database, database_exists



def main():
    check_database()
    
    print('Creating tables ...')
    Base.metadata.create_all(db.engine(), checkfirst=True)
    print('Tables are created!')
    
def check_database():       
    print('Checking if database exists ...')
    if not database_exists(db.db_url()):
        print('Database does not exist, creating it now ...')
        create_database(db.db_url())
        print('Database is created!')
    else:
        print('Database already exists.')
        
        
if __name__ == "__main__":
    main()

                
 

    
    