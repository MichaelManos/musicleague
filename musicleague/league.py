import os

import duckdb as dd
import pandas as pd

from musicleague import competitor, constants, utils
from musicleague.db import next_int


def delete_league(
    id: int,
    connection: dd.DuckDBPyConnection,
) -> None:
    """Deletes data for a single league from database

    Parameters
    ----------
    id : int
        ID of league to delete
    connection : duckdb.DuckDBPyConnection
        Connection to database
    """
    for table in constants.LEAGUE_TABLES:
        connection.execute(
            "DELETE FROM QUERY_TABLE(?) WHERE league_id = ?", [table, id]
        )
    connection.execute("DELETE FROM league WHERE id = ?", [id])


def insert_league(
    name: str,
    folder_path: str,
    connection: dd.DuckDBPyConnection,
) -> int:
    """Inserts league data into database. Will create a new league entry.

    Parameters
    ----------
    name : str
        Name of music league
    folder_path : str
        Directory containing exported data. Requires "competitors.csv",
        "rounds.csv", "submissions.csv", and "votes.csv" files to be present in
        the directory.
    connection : duckdb.DuckDBPyConnection
        Connection to database
    """
    id = new_record(name, connection)
    league_data = read_dir(folder_path)
    competitor.upsert_bulk(league_data["competitors"], connection)
    insert_league_data(league_data, connection, id)
    return id


def new_record(
    name: str,
    connection: dd.DuckDBPyConnection,
) -> int:
    id = next_int("league", connection)
    connection.execute(
        "INSERT INTO league (id, name) VALUES (?, ?)", [id, name]
    )
    return id


def read_dir(folder_path: str) -> dict[str, pd.DataFrame]:
    """Reads Music League export data into pandas DataFrames.

    Parameters
    ----------
    folder_path : str
        Directory containing exported data. Requires "competitors.csv",
        "rounds.csv", "submissions.csv", and "votes.csv" files to be present in
        the directory.

    Returns
    -------
    dict[str, pandas.DataFrame]
        Dictionary of DataFrames keyed by data set name ("rounds",
        "submissions", and so on). Column names are converted to snake case.
    """
    files_to_load = {}
    missing_files: list[str] = []
    for file in constants.LEAGUE_FILES:
        filename = f"{file}.csv"
        filepath = os.path.join(folder_path, filename)
        if os.path.exists(filepath):
            files_to_load[file] = filepath
        else:
            missing_files.append(filename)
    if len(files_to_load) < len(constants.LEAGUE_FILES):
        raise FileNotFoundError(
            f"Files missing from {folder_path}: {missing_files}"
        )
    return {
        file: pd.read_csv(files_to_load[file]).rename(columns=utils.to_snake)
        for file in files_to_load
    }


def insert_league_data(
    data: dict[str, pd.DataFrame], connection: dd.DuckDBPyConnection, id: int
) -> None:
    for table in constants.LEAGUE_TABLES:
        table_data = data[  # noqa: F841 - referenced via duckdb string
            f"{table}s"
        ].assign(league_id=id)
        connection.sql(f"INSERT INTO {table} BY NAME SELECT * FROM table_data")
