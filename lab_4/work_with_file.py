import json
import logging

from logging_config import setup_logging

setup_logging()


def read_json(name: str) -> dict:
    """
    Read JSON data from a file.

    Args:
        name (str): The path to the JSON file to read.

    Returns:
        dict: The JSON data read from the file.
    """
    try:
        logging.info(f"Reading JSON data from file: {name}")
        with open(name, "r", encoding="utf-8") as file:
            data = json.load(file)
        logging.info(f"Successfully read JSON data from file: {name}")
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {name}")
        print("File not found")
    except Exception as e:
        logging.error(f"Error reading file {name}: {str(e)}")
        print(f"Error reading file {str(e)}")


def write_to_json(file: str, data: dict) -> None:
    try:
        logging.info(f"Writing data to JSON file: {file}")
        with open(file, mode="w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logging.info(f"Successfully wrote data to JSON file: {file}")
    except Exception as e:
        logging.error(f"Error writing to file {file}: {str(e)}")
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
        logging.info(f"Reading binary data from file: {file_path}")
        with open(file_path, "rb") as file:
            data = file.read()
        logging.info(f"Successfully read binary data from file: {file_path}")
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        print("File not found")
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {str(e)}")
        print(f"Error reading file {str(e)}")


def write_bytes(file_path: str, bytes_text: bytes) -> None:
    """
    Writes binary data to a file.

    Parameters
        file_path: The path to the file where the data will be written.
        bytes_text: The binary data to be written to the file.
    """
    try:
        logging.info(f"Writing binary data to file: {file_path}")
        with open(file_path, "wb") as file:
            file.write(bytes_text)
        logging.info(f"Successfully wrote binary data to file: {file_path}")
        print(f"The data has been successfully written to the file '{file_path}'.")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        print("File not found")
    except Exception as e:
        logging.error(f"Error writing to file {file_path}: {str(e)}")
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
        logging.info(f"Reading text data from file: {name}")
        with open(name, 'r', encoding='utf-8') as file:
            data = file.read()
            logging.info(f"Successfully read text data from file: {name}")
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {name}")
        return "File not found"
    except Exception as e:
        logging.error(f"Error reading file {name}: {str(e)}")
        return f"Error reading file: {str(e)}"


def write_file(path: str, data: str) -> None:
    """
    A function for writing data to a file.

    Parameters
        path: the path to the file to write
        data: data to write to a file
    """
    try:
        logging.info(f"Writing data to file: {path}")
        with open(path, "w", encoding='UTF-8') as file:
            file.write(data)
        logging.info(f"Successfully wrote data to file: {path}")
        print(f"The data has been successfully written to the file '{path}'.")
    except FileNotFoundError:
        logging.error(f"File not found: {path}")
        print("File not found")
    except Exception as e:
        logging.error(f"Error writing to file {path}: {str(e)}")
        print(f"Error writing file {str(e)}")
