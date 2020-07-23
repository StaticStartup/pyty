# coding: utf-8

""" SQLite Module

Enables connectivity with SQLite.

Classes
-----------
sqlite: Enables connectivity with SQLite.
"""

# Standard Library
import sqlite3
from contextlib import closing

# Third Party Library
import pandas


class sqlite():
    def __init__(self, db_file: str):
        """
        Create a connection to the SQLite database specified by db_file
            :param db_file: database file
            :return: None
        """
        if not db_file:
            raise ConnectionError("Please specify the database name!")
        self.conn = sqlite3.connect(db_file)

    def createFromSQL(self, sql: str):
        """
        Create a table from the sql statement
            :param sql: CREATE TABLE statement
            :return: None
        """
        with closing(self.conn):
            self.conn.cursor().execute(sql)

    def createFromPandas(self, data: pandas.DataFrame, table_name: str, table_schema: str = None, if_exists: str = 'fail', index: bool = True, index_label: str = None, chunksize: int = None, dtype: dict = None):
        pass

    def createFromExcel(self, data_file: str, table_name: str, table_schema: str = None, if_exists: str = 'fail', index: bool = True, index_label: str = None, chunksize: int = None, dtype: dict = None):
        pass
