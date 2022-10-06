from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker       

from dotenv import load_dotenv
import os       

load_dotenv()

db_user = os.environ["DB_USER"]
db_pass = os.environ["DB_PASS"]
db_host = os.environ["DB_HOST"]
db_name = os.environ["DB_NAME"]


# engine = create_engine("postgresql://mysuperuser2:123@localhost/flask", echo=True)
engine = create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}", echo=True)
conn = engine.connect()
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


        # user = Users.query.filter_by(email=email).first()
