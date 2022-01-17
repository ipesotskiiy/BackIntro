from src.schemas import TestTableSchema
from src.connections.connect_module import *



class Requests(Connection):
    def __init__(self):
        Connection.__init__(self)

    def create_table(self):
        self.database_sql_req('CREATE TABLE test_table1 ('
                              '"id" SERIAL PRIMARY KEY,'
                              '"first_name" TEXT NOT NULL,'
                              '"last_name" TEXT NOT NULL,'
                              '"age" TEXT NOT NULL);')

    def read_table(self):
        read_table = self.database_sql_req('SELECT * '
                              'FROM test_table1;', results=True)
        return read_table

    def update_table(self, req_dict:TestTableSchema):
        self.database_sql_req('INSERT INTO test_table1 (first_name, last_name, age) '
                              f'VALUES (\'{req_dict.first_name}\',\'{req_dict.last_name}\',\'{req_dict.age}\'); ')

    def drop_table(self):
        self.database_sql_req('DROP TABLE test_table1;')




