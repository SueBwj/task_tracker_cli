# Set Up the Database Configuration 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://Sue:Wj_040217@localhost/testdb', echo=False)

Session = sessionmaker(bind=engine)