from database.database import Base
from sqlalchemy import Column, String

class Users(Base):
    __tablename__ = "users"
    
    name = Column(String, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    
    def __repr__(self):
        return f"Nome={self.name}, Email={self.email}"

    # def json(self):
    #     return {'email': self.email,
                
    #             'nome': self.nome}
        
        
    # @classmethod 
    # def buscar_todos_usuarios(cls):
    #     resultado = session.query(UsuarioModel).all() usuarios = [usuario.json() for usuario in resultado] 
    #     return usuarios 