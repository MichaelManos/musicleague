import duckdb as dd
import pandas as pd


def upsert_bulk(
    data: pd.DataFrame,
    connection: dd.DuckDBPyConnection,
):
    """Upserts multiple competitor records from a single DataFrame"""
    for _, row in data.iterrows():
        upsert(row, connection)


def upsert(
    competitor: pd.Series | dict,
    connection: dd.DuckDBPyConnection,
) -> None:
    """Inserts new record for the competitor if record does not exist.
    Otherwise updates the name at the given ID. ("Upsert" operation)

    Parameters
    ----------
    competitor : pandas.Series or dict
        Competitor data to insert or update. Requires "name" and "id" fields.
    table : str
        Table to insert or update
    connection : duckdb.DuckDBPyConnection
        Connection to database
    check_col : str, default "name"
        Column name to check for equality

    Returns
    -------
    bool
        True if insert, False if update
    """
    name = competitor["name"]
    id = competitor["id"]
    result = connection.execute(
        "SELECT 1 FROM competitor WHERE id = ?", [id]
    ).fetchdf()
    if len(result) == 0:
        connection.execute(
            "INSERT INTO competitor (id, name) VALUES(?, ?);", [id, name]
        )
        return
    connection.execute(
        "UPDATE competitor SET name = ? WHERE id = ?;", [name, id]
    )
