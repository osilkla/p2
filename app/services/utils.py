from const import CSV_HEADER, RATING_RANGE
import csv


def init_directory(os, directoryName: str):
    if not os.path.exists(directoryName):
        os.makedirs(directoryName)


def add_header_to_CSV(csvUrl: str):
    with open(csvUrl, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_HEADER)
        writer.writeheader()


def add_row_to_CSV(csvUrl: str, book: dict):
    with open(csvUrl, "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_HEADER)
        writer.writerow(book)


def sanitize_string(str: str) -> str:
    return f'"{str}"'


def convert_abc_rating_score_to_123(string_rating_score: str) -> str:
    return RATING_RANGE.get(string_rating_score, "Null")