import glob
import os

import duckdb as dd


def connect(path: str) -> dd.DuckDBPyConnection:
    """Creates or connects to a database at `path`"""
    con = dd.connect(path)
    return con


def create_all(connection: dd.DuckDBPyConnection):
    """Creates database objects on `connection`"""
    sql_dir = os.path.join(os.path.dirname(__file__), "..", "ddl")
    object_files = glob.glob(os.path.join(sql_dir, "*.sql"))
    for file in object_files:
        with open(file, "r") as sql:
            connection.sql(sql.read())
