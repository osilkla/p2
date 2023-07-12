import os
import re
from const import CSV_HEADER, CSV_DELIMITER, IMG_DIRECTORY
import csv

RATING_RANGE = {
    "One": "1",
    "Two": "2",
    "Three": "3",
    "Four": "4",
    "Five": "5",
}


def init_directory(os, directoryName: str) -> None:
    if not os.path.exists(directoryName):
        os.makedirs(directoryName)


def add_header_to_CSV(csvUrl: str) -> None:
    with open(csvUrl, "w") as csv_file:
        writer = csv.DictWriter(
            csv_file, fieldnames=CSV_HEADER, delimiter=CSV_DELIMITER
        )
        writer.writeheader()


def add_row_to_CSV(csvUrl: str, book: dict) -> None:
    with open(csvUrl, "a") as csv_file:
        writer = csv.DictWriter(
            csv_file, fieldnames=CSV_HEADER, delimiter=CSV_DELIMITER
        )
        writer.writerow(book)


def sanitize_string(str: str) -> str:
    return f'"{str}"'


def convert_abc_rating_score_to_123(string_rating_score: str) -> str:
    return RATING_RANGE.get(string_rating_score, "Null")


def get_local_img_src(book_title: str, category_name: str):
    img_directory_with_category_name = os.path.join(IMG_DIRECTORY, category_name)
    init_directory(os, img_directory_with_category_name)
    image_title = re.sub("[^a-zA-Z0-9 \n]", "", book_title)
    return os.path.join(img_directory_with_category_name, f"{image_title}.jpg")
