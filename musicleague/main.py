import os

import pandas as pd

from musicleague import constants


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
        "submissions", and so on)
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
    return {file: pd.read_csv(files_to_load[file]) for file in files_to_load}
