from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost/app1"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
        db.commit()  # Commit if everything goes well
    except Exception:
        db.rollback()  # Rollback if there's an exception
        raise  # Re-raise the exception so it can be handled by FastAPI
    finally:
        db.close()  # Close the session
