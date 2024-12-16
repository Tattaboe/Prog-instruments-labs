import os
from typing import Optional

import csv
from tqdm import trange


def first_script(path_dir: str) -> None:
    """create csv """
    out_directory = os.path.dirname(__file__)
    with open("classmates1.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(["Абсолютный путь к файлу", "Относительный путь к файлу", "номер звезды"])
        for star in trange(1, 6):
            directory = os.path.join(out_directory, "dataset", str(star))
            for dirs, folder, files in os.walk(directory):
                for element in files:
                    file_writer.writerow([str(dirs) + "/" + element, "dataset"+'/' + str(star) + "/" + element, star])


def script_1(name: str) -> None:
    """create a csv"""
    first_script(name)


if __name__ == "__main__":
    script_1("rt")