import glob
import os

import duckdb as dd
import pandas as pd


def connect(path: str) -> dd.DuckDBPyConnection:
    """Creates or connects to a database at `path`.

    If the database does not already exist, the necessary music league schema
    will be created."""
    create_tables = False
    if not os.path.exists(path):
        create_tables = True
    con = dd.connect(path)
    if create_tables:
        create_all(con)
    return con


def create_all(connection: dd.DuckDBPyConnection) -> None:
    """Creates database objects on `connection`"""
    sql_dir = os.path.join(os.path.dirname(__file__), "..", "ddl")
    object_files = glob.glob(os.path.join(sql_dir, "*.sql"))
    for file in object_files:
        with open(file, "r") as sql:
            connection.sql(sql.read())


def next_int(
    table: str,
    connection: dd.DuckDBPyConnection,
    primary_key: str = "id",
) -> int:
    """Returns the next integer available in a sequence. Used to generate
    primary keys. (This is a naive function that assumes no race conditions.)

    Parameters
    ----------
    table : str
        Name of table to check
    connection : duckdb.DuckDBPyConnection
        Connection to database
    primary_key : str, default "id"
        Name of primary key column

    Returns
    -------
    int
        Next available integer
    """
    result = (
        connection.execute(
            "SELECT MAX(COLUMNS(?)) FROM QUERY_TABLE(?)", [primary_key, table]
        )
        .fetchdf()
        .iloc[0, 0]
    )
    if pd.isna(result):
        return 1
    return int(result) + 1


def start_ui(connection: dd.DuckDBPyConnection) -> None:
    """Starts the DuckDB user interface

    Parameters
    ----------
    connection : duckdb.DuckDBPyConnection
        Connection to database
    """
    connection.sql("CALL start_ui();")
