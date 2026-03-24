import json


def load_data(file_path: str):
    """
    Load data from a JSON file.

    Args:
        file_path: Path to the JSON file.

    Returns:
        Data loaded from the JSON file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"{file_path} does not exist.")
    except PermissionError:
        print(f"Cannot read file {file_path}. Permission denied.")
    except UnicodeDecodeError:
        print(f"Cannot read file {file_path}. Encoding should be UTF-8.")
    except OSError as e:
        print(f"Failed to load {file_path}: {e}")
    return None


def print_animal(animal: dict):
    """
    Print available information about an animal (name, diet, location and type).

    Args:
        animal: dictionary with the data about the animal.
    """
    if animal.get("name"):
        print(f"Name: {animal["name"]}")
    if animal.get("characteristics", {}).get("diet"):
        print(f"Diet: {animal["characteristics"]["diet"]}")
    if animal.get("locations"):
        print(f"Location: {animal["locations"][0]}")
    if animal.get("characteristics", {}).get("type"):
        print(f"Type: {animal["characteristics"]["type"]}")


def main():
    animals = load_data("animals_data.json")
    print_animal(animals[0])


if __name__ == "__main__":
    main()
