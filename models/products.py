from database.database import Base, session, engine
from sqlalchemy import Column, String, Integer, Boolean, Numeric


class ProductsModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    category = Column(String, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Numeric(5,2), nullable=False)
    desc_price = Column(Numeric(5,2), nullable=False)
    sku = Column(String, nullable=False)
    route = Column(String, nullable=False)
    alt_img = Column(String, nullable=False)
    img_main = Column(String, nullable=False)
    img_front = Column(String, nullable=False)
    img_right = Column(String, nullable=False)
    img_left = Column(String, nullable=False)
    img_back = Column(String, nullable=False)
    highlights = Column(Boolean, default=False)
    is_available = Column(Boolean, default=True)

    def __init__(self, category, name, price, desc_price, sku, route, alt_img, img_main, img_front, img_right, img_left, img_back):
        self.category = category
        self.name = name
        self.price = price
        self.desc_price = desc_price
        self.sku = sku
        self.route = route
        self.alt_img = alt_img
        self.img_main = img_main
        self.img_front = img_front
        self.img_right = img_right
        self.img_left = img_left
        self.img_back = img_back

    def json(self):
        return {
            'id': self.id,
            'category': self.category,
            'name': self.name,
            'price': f'{self.price}',
            'desc_price': f'{self.desc_price}',
            'sku': self.sku,
            'route': self.route,
            'alt_img': self.alt_img,
            'img_main': self.img_main,
            'img_front': self.img_front,
            'img_right': self.img_right,
            'img_left': self.img_left,
            'img_back': self.img_back
        }


    @classmethod
    def product_id(cls):
        product = session.query(ProductsModel).first()
        
        if product:
            return product
        return None

    # TODOS OS PRODUTOS
    @classmethod
    def products_total(cls):
        result = session.query(ProductsModel).filter_by(is_available='TRUE').all()        
        products = [product.json() for product in result]
        return products
    
    #  PRODUTOS DESTAQUE
    @classmethod
    def products_highlights(cls):
        result = session.query(ProductsModel).filter_by(highlights='TRUE', is_available='TRUE').all()        
        products = [product.json() for product in result]
        return products

    # PRODUTOS MASCULINOS
    @classmethod
    def products_masculino(cls):
        result = session.query(ProductsModel).filter_by(category='masculino', is_available='TRUE').all()        
        products = [product.json() for product in result]
        
        return products
    
    # PEODUTOS FEMININO
    @classmethod
    def products_feminino(cls):
        result = session.query(ProductsModel).filter_by(category='feminino', is_available='TRUE').all()        
        products = [product.json() for product in result]
        
        return products
    
    # PRODUTOS CALÇADOS
    @classmethod
    def products_calcados(cls):
        result = session.query(ProductsModel).filter_by(category='calcados', is_available='TRUE').all()               
        products = [product.json() for product in result]
        
        return products
    
    # PRODUTOS ACESSÓRIOS
    @classmethod
    def products_acessorios(cls):
        result = session.query(ProductsModel).filter_by(category='acessorios', is_available='TRUE').all()    
        products = [product.json() for product in result]
        
        return products


Base.metadata.create_all(engine)
