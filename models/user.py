from database.database import Base, engine, session
from sqlalchemy import Column, String, Integer, ForeignKey
# from models.products import ProductsModel


class UsersModel(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
#     # product_id = Column(Integer, ForeignKey("ProductsModel",backref="users")) Froma correta
#     # product_id = Column(Integer, ForeignKey(ProductsModel.id)) Forçando / nao usar se nao for necessário

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def json(self):

        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email
        }

    def json_login(self):

        return {
            "user_id": self.user_id,
            "email": self.email
        }

    @classmethod
    def find_users(cls):
        result = session.query(UsersModel).all()
        users = [user.json() for user in result]
        return users

    @classmethod
    def find_user(cls, user_id):
        user = session.query(UsersModel).filter_by(user_id=user_id).first()
        if user:
            return user
        return None

    @classmethod
    def find_user_email(cls, email):
        user = session.query(UsersModel).filter_by(email=email).first()
        if user:
            return user
        return None

    def hash_password(self, password):
        from app import bcrypt

        hashed = bcrypt.generate_password_hash(password).decode('utf-8')
        self.password = hashed

    def update_user(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def save_user(self):
        session.add(self)
        session.commit()

    def delete_user(self):
        session.delete(self)
        session.commit()


Base.metadata.create_all(engine)
