import os
import inquirer
from services.book_scraper import (
    get_categories_list,
    save_books_in_csv,
)
from services.utils import init_directory
from const import (
    CSV_DIRECTORY,
    USER_CHOICES,
    USER_CHOICE_SCRAP_ALL,
    USER_CHOICE_SCRAP_CAT,
    USER_YES_NO_CHOICES,
)


print("What do you want to do ?")
user_choice = input(
    "Type 'All' if you want to srap all books, Type 'Category' if you want to scrap only one Category: "
).upper()

if user_choice not in USER_CHOICES:
    print("This input is not a valid choice", user_choice)


init_directory(os, CSV_DIRECTORY)
categories = get_categories_list()

if user_choice == USER_CHOICE_SCRAP_ALL:
    for category, url in categories.items():
        save_books_in_csv(url, category)


elif user_choice == USER_CHOICE_SCRAP_CAT:
    user_want_to_scrap = True
    while user_want_to_scrap:
        category_question = [
            inquirer.List(
                "category",
                message="What category do you want to extract?",
                choices=categories.keys(),
            ),
        ]
        category_name = inquirer.prompt(category_question)["category"]
        user_category_url = categories[category_name]
        save_books_in_csv(user_category_url, category_name)

        continue_or_quit_question = [
            inquirer.List(
                "continue",
                message="Do you want to extract an other one?",
                choices=USER_YES_NO_CHOICES,
            ),
        ]
        user_choice = inquirer.prompt(continue_or_quit_question)["continue"]
        user_want_to_scrap = user_choice == USER_YES_NO_CHOICES[0]
        if not user_want_to_scrap:
            break
