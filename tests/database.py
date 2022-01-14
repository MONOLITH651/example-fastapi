import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from starlette.responses import Response
from app.main import app
from app.config import settings
from alembic import command
from app.database import get_db, Base

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost:5432/fastapi_test"
# hardcoding 
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'
# making same as .env
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(app)

@pytest.fixture()
def session():
    print("my session fixture ran")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
        def override_get_db():
            try:
                yield session
            finally:
                session.close()
        app.dependency_overrides[get_db] = override_get_db
        yield TestClient(app)
        # now you can make queries
        # and you have access to the client
        # when you call client the session will run first
        # then the client runs
