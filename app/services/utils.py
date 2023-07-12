import os
import re
import csv

from const import CSV_HEADER, CSV_DELIMITER, IMG_DIRECTORY

RATING_RANGE = {
    "One": "1",
    "Two": "2",
    "Three": "3",
    "Four": "4",
    "Five": "5",
}

ALLOW_ONLY_NUMBER_AND_LETTERS = "[^a-zA-Z0-9 \n]"
REPLACE_SPACE = "\s"


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


def format_string_to_acceptable_file_name(input_string: str):
    formatted_string = input_string[:31]
    formatted_string = re.sub(ALLOW_ONLY_NUMBER_AND_LETTERS, "", formatted_string)
    formatted_string = formatted_string.strip()
    formatted_string = re.sub(REPLACE_SPACE, "-", formatted_string)
    formatted_string = formatted_string.lower()
    return formatted_string


def get_local_img_src(book_title: str, category_name: str):
    img_directory_with_category_name = os.path.join(IMG_DIRECTORY, category_name)
    init_directory(os, img_directory_with_category_name)
    image_title = format_string_to_acceptable_file_name(book_title)
    return os.path.join(img_directory_with_category_name, f"{image_title}.jpg")
