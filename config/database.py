from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from models.user import Users


engine = create_engine("postgresql://mysuperuser2:123@localhost/flask", echo=True)
conn = engine.connect()
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

eMail = "henriquef@emial.com"

session.query(Users).filter(Users.email == {eMail})
        # user = Users.query.filter_by(email=email).first()
