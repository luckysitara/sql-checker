#!/usr/bin/python3
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

class SQLiteSQLGrader:
    def __init__(self, sqlite_db):
        self.connection = sqlite3.connect(sqlite_db)
        self.metadata = MetaData(bind=self.connection)
        self.test_cases_table = Table('test_cases', self.metadata, 
                                     Column('id', Integer, primary_key=True),
                                     Column('query', String),
                                     Column('score', Integer))

    def create_test_case(self, query, score):
        self.test_cases_table.create()
        ins = self.test_cases_table.insert().values(query=query, score=score)
        self.connection.execute(ins)

    def evaluate_student_sql(self, student_query):
        try:
            # Implement your comparison and scoring logic here
            # For simplicity, just return a placeholder score
            return 90

        except Exception as e:
            print(f"Error: {e}")

    def close_connection(self):
        self.connection.close()

