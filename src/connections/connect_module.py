import psycopg2
from psycopg2 import Error
import os


class Connection:
    def __init__(self):
        self.connection = psycopg2.connect(user="postgres",
                                           password="postgres",
                                           host="postgres",
                                           port="5432",
                                           database="postgres")
        self.cursor = self.connection.cursor()

    def database_sql_req(self, command, results=False):
        """
        Метод для написания SQL-запросов напрямую

        :param command: SQL-запрос
        :param results: указать True, если нужен вывод результатов
        :return:
        """
        try:
            self.cursor.execute(command)
            self.connection.commit()

            if results:
                data = self.cursor.fetchall()
                return data

        except (Exception, Error) as error:
            print('!!! Ошибка !!!', error)

    def restart_connection(self):
        self.cursor.close()
        self.connection.close()
        self.connection = psycopg2.connect(user="postgres",
                                           password="postgres",
                                           host="postgres",
                                           port="5432",
                                           database="postgres")
        self.cursor = self.connection.cursor()

