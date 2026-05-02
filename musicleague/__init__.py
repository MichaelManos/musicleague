"""Utility for reading and organizing Music League data

Core functions (use help(...) to examine use):
- **connect**: Connect to an existing duckdb database file. If path does not
  exist, this will create a new one at the path. Or use ":memory:" for a
  temporary, in-memory database.
- **insert_league**: Insert league data into database
- **delete_league**: Remove league data from database
- **export**: Export database contents to analytical data set
- **start_ui**: Open web UI to explore database interactively
"""

from musicleague._version import __version__  # noqa: F401
from musicleague.db import connect, create_all, export, start_ui  # noqa: F401
from musicleague.league import delete_league  # noqa: F401
from musicleague.league import insert_league  # noqa: F401
from musicleague.league import read_dir  # noqa: F401
