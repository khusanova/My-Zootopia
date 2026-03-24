import json


ANIMALS_JSONFILE = "animals_data.json"


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


def get_animal_information(animal: dict) -> str:
    """
    Export available information about an animal (name, diet, location and
    type) to string.

    Args:
        animal: Dictionary with the data about the animal.

    Returns:
        String with available information about the animal.
    """
    animal_info = ""
    if animal.get("name"):
        animal_info += f"Name: {animal["name"]}\n"
    if animal.get("characteristics", {}).get("diet"):
        animal_info += f"Diet: {animal["characteristics"]["diet"]}\n"
    if animal.get("locations"):
        animal_info += f"Location: {animal["locations"][0]}\n"
    if animal.get("characteristics", {}).get("type"):
        animal_info += f"Type: {animal["characteristics"]["type"]}\n"
    return animal_info


def print_animals():
    """
    Load and print information about animals in the database.
    """
    animals = load_data(ANIMALS_JSONFILE)
    for animal in animals:
        print(get_animal_information(animal))


def main():
    print_animals()


if __name__ == "__main__":
    main()
