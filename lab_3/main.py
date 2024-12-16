import csv
import re

from checksum import calculate_checksum, serialize_result

VARIANT = 69

PATTERNS = {
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "http_status_message": "^\d{3} [A-Za-z ]+$",
    "inn": "^\d{12}$",
    "passport": "^\d{2} \d{2} \d{6}$",
    "ip_v4": "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|"
             "[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",
    "latitude": "^(-?[1-8]?\d(?:\.\d{1,})?|90(?:\.0{1,})?)$",
    "hex_color": "^#[0-9a-fA-F]{6}$",
    "isbn": "(\d{3}-)?\d-(\d{5})-(\d{3})-\d",
    "uuid": "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$",
    "time": "^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.(\d{1,6})$"
}


def check_invalid_row(row: list) -> bool:
    """
        Функция проверки каждой строки на валидность
    """
    for patterns, item in zip(PATTERNS.keys(), row):
        if not re.search(PATTERNS[patterns], item):
            return False
    return True


def get_no_invalid_data_index(data: list) -> list:
    """
        Функция находит невалидные строки и записывает их индексы
    """
    data_index = []
    index = 0
    for row in data:
        if not check_invalid_row(row):
            data_index.append(index)
        index += 1
    return data_index


if __name__ == "__main__":
    '''
        Считывание csv файла и запись checksum
    '''
    data = []
    with open("69.csv", "r", newline="", encoding="utf-16") as file:
        read_data = csv.reader(file, delimiter=";")
        for row in read_data:
            data.append(row)
    data.pop(0)
    serialize_result(VARIANT, calculate_checksum(
        get_no_invalid_data_index(data)))
