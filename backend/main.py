from fastapi import FastAPI
from core.config import setting
from db.session import engine
from db.base import Base

import uvicorn


def create_table():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=setting.PROJECT_NAME, version=setting.PROJECT_VERSION)
    create_table()
    return app

app = start_application()


@app.get('/')
async def root():
    return {'msg': 'Hello world!🚀'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
