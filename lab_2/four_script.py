import csv


def four_script(star):
    """create csv"""
    with open("classmates3.csv", "r") as fh:
        reader = csv.reader(fh)  # (!) обратите внимание, что reader возвращает итератор
        spisok = list(reader)  # поэтому мы делаем приведение к типу list
    for element in spisok:
        if element[2] == str(star):
            print(element[0])


if __name__ == "__main__":
    four_script(3)