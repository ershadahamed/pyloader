import uvicorn
import logging
from fastapi import FastAPI, Depends
from config import config, database
from schemas.UserSchema import UserSchema
from models import create_models
from models.User import User
from sqlalchemy.orm import Session

create_models.run_models()

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def root():
    data = {
        'title': 'Main Page',
        'text': 'Ok'
    }

    return data


@app.post('/create/user')
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = User(name=user.name, email=user.email, hashed_password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def log():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(config.format_type)
    file_handler = logging.FileHandler(config.path)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=80, reload=True)
