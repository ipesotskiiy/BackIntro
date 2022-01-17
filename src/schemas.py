from pydantic import BaseModel

class TestTableSchema(BaseModel):
    first_name : str
    last_name : str
    age : int