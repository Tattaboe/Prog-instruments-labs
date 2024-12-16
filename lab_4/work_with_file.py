import json


def read_json(name: str) -> dict:
    """
    Read JSON data from a file.

    Args:
        name (str): The path to the JSON file to read.

    Returns:
        dict: The JSON data read from the file.
    """
    try:
        with open(name, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error reading file {str(e)}")


def write_to_json(file: str, data: dict) -> None:
    try:
        with open(file, mode="w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error reading file {str(e)}")


def read_bytes(file_path: str) -> bytes:
    """
    Reads the contents of a file in binary format.

    Parameters
        file_path: The path to the file to be read.
    Returns
        The contents of the file in binary format.
    """
    try:
        with open(file_path, "rb") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error reading file {str(e)}")


def write_bytes(file_path: str, bytes_text: bytes) -> None:
    """
    Writes binary data to a file.

    Parameters
        file_path: The path to the file where the data will be written.
        bytes_text: The binary data to be written to the file.
    """
    try:
        with open(file_path, "wb") as file:
            file.write(bytes_text)
        print(f"The data has been successfully written to the file '{file_path}'.")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error writing file {str(e)}")


def read_file(name: str) -> str:
    """
    Read text data from a file.

    Args:
        name (str): The path to the file to read.

    Returns:
        str: The text data read from the file.
    """
    data = ""
    try:
        with open(name, 'r', encoding='utf-8') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error reading file: {str(e)}"


def write_file(path: str, data: str) -> None:
    """
    A function for writing data to a file.

    Parameters
        path: the path to the file to write
        data: data to write to a file
    """
    try:
        with open(path, "w", encoding='UTF-8') as file:
            file.write(data)
        print(f"The data has been successfully written to the file '{path}'.")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error writing file {str(e)}")