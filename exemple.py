# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
# from config.database import Base, session
# from models.user import Users
# from sqlalchemy import Column, String


# engine = create_engine("postgresql://mysuperuser2:123@localhost/flask", echo=True)
# conn = engine.connect()
# Base = declarative_base()

# Session = sessionmaker(bind=engine)
# session = Session()


# class Users(Base):
#     __tablename__ = "users"
    
#     name = Column(String, primary_key=True)
#     email = Column(String)
#     password = Column(String)
    
#     def __repr__(self):
#         return f"Nome={self.name}, Email={self.email}"

#SQL

#INSERT

# data_insert = Users(name="teste", email="testye@teste.com", password="kldsjfsdkj")
# session.add(data_insert)
# session.commit()

# session.close()

#UPDATE
# session.query(Users).filter(Users.name=="teste").update({ "name": "cleiton" })
# session.commit()


#DELETE
# session.query(Users).filter(Users.name=="henrique").delete()
# session.commit

# session.close()


#SELECT

# data = session.query(Users).all()
# eMail = "henriquef@emial.com"

# data = session.query(Users).filter(Users.email == {eMail})
# print(data)

# session.close()
