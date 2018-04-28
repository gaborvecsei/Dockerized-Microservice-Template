import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

user = os.environ['POSTGRES_USER']
pwd = os.environ['POSTGRES_PASSWORD']
db = os.environ['POSTGRES_DB']
# Docker creates hostnames from the service names defined in docker-compose
host = os.environ['DB_DOCKER_SERVICE_NAME']
port = os.environ['DB_PORT']

engine = create_engine("postgres://{0}:{1}@{2}:{3}/{4}".format(user, pwd, host, port, db))

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
