from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#create a database  URL for SQLAlquemy
SQLALCHEMY_DATABASE_URL = "sqlite:////home/ayelen/Documentos/Python/taskAPI/app/taskapiPython.sqlite"


#create a SQLAlchemy engine , connect_arg is needed only for SQLlite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#create a SessionLocal class. 
#Each instance of sessionLocal class will be a database session. The class itself is not a database session yet
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Create a Base class. Later we will inherit from this class to create each of the database models or classes )the ORM models)
Base = declarative_base()

