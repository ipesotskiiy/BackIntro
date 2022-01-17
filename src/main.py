# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import uvicorn
from fastapi import FastAPI, Form
from typing import Any, Dict, List

from src.connections.requests_module import *

MyClass = Requests()

app = FastAPI()


@app.get("/")
async def root():
    return 'Сервис готов к работе.'


@app.post("/update_database/")
async def update_endpoint(request: TestTableSchema):
    try:
        MyClass.update_table(request)
    except Exception as err:
        return err

    return 'База данных успешно обновлена'


@app.get("/create_database/")
async def create_endpoint():
    try:
        MyClass.create_table()
    except Exception as err:
        return err

    return 'База данных успешно создана'


@app.get("/read_database/")
async def read_endpoint():
    try:
        read_data = MyClass.read_table()
    except Exception as err:
        return err

    return 'База данных успешно открыта для чтения', read_data


@app.get("/drop_database/")
async def drop_endpoint():
    try:
        MyClass.drop_table()
    except Exception as err:
        return err

    return 'База данных успешно удалена'


@app.get("/restart_database/")
async def restart_endpoint():
    try:
        MyClass.restart_connection()
    except Exception as err:
        return err

    return 'База данных успешно удалена'


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
