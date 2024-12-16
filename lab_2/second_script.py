import os
from typing import Optional

import csv


import first_script

def second_script(path: str) -> str:
    #read csv and copy dataset .../1/0001.txt =.../1_0001.txt
    if os.path.exists('classmates1.csv') == False:
        first_script.first_script("")
    with open("classmates1.csv", "r") as fh:
        reader = csv.reader(fh)  # (!) обратите внимание, что reader возвращает итератор
        spisok = list(reader)  # поэтому мы делаем приведение к типу list
    if os.path.isdir("second_dataset") == False: os.makedirs("second_dataset")
    content = False
    for element in spisok:
        if content:
            with open(element[0], "rb") as f:
                text = f.read()
                namefile = element[1].split("/")
            with open(os.path.join("second_dataset", element[2] + "_" + namefile[2]), "wb") as f:
                f.write(text)
        content = True

def script_2(name: str) -> None:
    """create a csv"""
    second_script(name)


if __name__=="__main__":
    script_2("rt")