import json


def load_data(file_path: str):
    """
    Load data from a JSON file.

    Args:
        file_path: Path to the JSON file.

    Returns:
        Data loaded from the JSON file.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)