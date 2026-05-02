def to_snake(string: str) -> str:
    """Converts string to snake case. Specifically:

    - Converts to lower case
    - Replaces spaces with underscores
    - Removes noted special characters
    """
    string = string.lower()
    string = string.replace(" ", "_")
    string = string.replace("(", "")
    string = string.replace(")", "")
    return string
