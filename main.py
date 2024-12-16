from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
connection_str = 'mysql+mysqlconnector://Jedidah:Backcase#123@localhost/tech4girls'

engine = create_engine(connection_str)

try:
    connection = engine.connect()
    print('Located and connected to databases')
    connection.close()
except Exception as e:
    print(f'An error occured: {e}')    

DBSession = sessionmaker(bind=engine)
session = DBSession()