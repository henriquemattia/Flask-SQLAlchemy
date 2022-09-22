from config.database import Base
from sqlalchemy import Column, String

class Users(Base):
    __tablename__ = "users"
    
    name = Column(String, primary_key=True)
    email = Column(String)
    password = Column(String)
    
    def __repr__(self):
        return f"Nome={self.name}, Email={self.email}"
