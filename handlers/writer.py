import csv

from typing import Any


class CsvWriter:
    @staticmethod
    def write(path: str, data: list[list[Any]]):
        with open(path, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(data)
