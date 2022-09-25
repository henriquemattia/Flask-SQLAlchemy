from database import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey

class Products(Base):
    __tablename__ = "produtos"
    
    id = Column(Integer, primary_key=True)
    categoria = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    preco = Column(String, nullable=False)
    desc_preco = Column(String, nullable=False)
    rota = Column(String, nullable=False)
    img_id = Column(Integer, ForeignKey("img_id"))
    destaque = Column(Boolean, nullable=False, default=False)
    is_available = Column(Boolean, nullable=False, default=True)
    # img = relationship("imagens")
    
class Imagens(Base):
    __tablename__ = "imagens"
    
    id = Column(Integer, primary_key=True)
    img_main = Column(String, nullable=False)
    img_front = Column(String, nullable=False)
    img_right = Column(String, nullable=False)
    img_left = Column(String, nullable=False)
    img_back = Column(String, nullable=False)
    
