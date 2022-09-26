from database.database import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Products(Base):
    __tablename__ = "produtos"
    
    id = Column(Integer, primary_key=True)
    categoria = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    preco = Column(String, nullable=False)
    desc_preco = Column(String, nullable=False)
    rota = Column(String, nullable=False)
    img_id = Column(Integer, ForeignKey("images.id"))
    destaque = Column(Boolean, nullable=False, default=False)
    is_available = Column(Boolean, nullable=False, default=True)
    images = relationship("Imagens")
    
class Imagens(Base):
    __tablename__ = "images"
    
    id = Column(Integer, primary_key=True)
    img_main = Column(String, nullable=False)
    img_front = Column(String, nullable=False)
    img_right = Column(String, nullable=False)
    img_left = Column(String, nullable=False)
    img_back = Column(String, nullable=False)
    
