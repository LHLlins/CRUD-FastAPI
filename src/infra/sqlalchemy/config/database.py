from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#Conexão com banco de dados
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Brasil87@localhost:5433/dynamov"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
#
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def criar_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  