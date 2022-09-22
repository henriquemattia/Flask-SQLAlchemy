from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from sqlalchemy import Column, String


engine = create_engine("postgresql://mysuperuser2:123@localhost/flask", echo=True)
conn = engine.connect()
Base = declarative_base()

# Session = sessionmaker(bind=engine)
# session = Session()


class Users(Base):
    __tablename__ = "users"
    
    name = Column(String, primary_key=True)
    email = Column(String)
    password = Column(String)
    
    def __repr__(self):
        return f"Nome={self.name}, Email={self.email}"
