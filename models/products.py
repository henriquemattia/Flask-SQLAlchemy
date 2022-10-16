from database.database import Base, session, engine
from sqlalchemy import Column, String, Integer, Boolean, Float


class ProductsModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    category = Column(String, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Float(2), nullable=False)
    desc_price = Column(Float(2), nullable=False)
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
            'price': self.price,
            'desc_price': self.desc_price,
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
    def find_products(cls):
        result = session.query(ProductsModel).all()
        products = [product.json() for product in result]
        return products

    @classmethod
    def product_id(cls):
        product = session.query(ProductsModel).first()

        if product:
            return product
        return None

    def highlights_true(self):
        result = session.execute(
            "SELECT * FROM products WHERE highlights = 'TRUE' AND is_available = 'TRUE'")
        products = [product.json() for product in result]
        return products

    def products_masculino(self):
        # result = session.query(ProductsModel).filter_by(category=category).filter(self.is_available == True).all()
        result = session.execute("SELECT * FROM products WHERE category = 'masculino' AND is_available = 'TRUE'")
        products = [product.json() for product in result]
        return products


Base.metadata.create_all(engine)
