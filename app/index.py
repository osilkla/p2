import os
from display_choices_menu import (
    display_extract_all_or_category_menu_to_user,
    display_extract_one_category_menu_to_user,
    display_continue_or_quit_menu,
    USER_CHOICE_SCRAP_ALL,
    USER_CHOICE_SCRAP_CAT,
    USER_YES_NO_CHOICES,
)
from services.book_scraper import (
    get_categories_list,
    save_books_in_csv,
)
from services.utils import init_directory
from const import (
    CSV_DIRECTORY,
)

instruction_is_set = False


while not instruction_is_set:
    user_choice = display_extract_all_or_category_menu_to_user()
    instruction_is_set = bool(user_choice)


init_directory(os, CSV_DIRECTORY)
categories = get_categories_list()

if user_choice == USER_CHOICE_SCRAP_ALL:
    for category, url in categories.items():
        save_books_in_csv(url, category)


elif user_choice == USER_CHOICE_SCRAP_CAT:
    user_want_to_scrap = True
    while user_want_to_scrap:
        user_category_url, category_name = display_extract_one_category_menu_to_user(
            categories
        )
        save_books_in_csv(user_category_url, category_name)
        user_choice = display_continue_or_quit_menu()

        user_want_to_scrap = bool(user_choice == USER_YES_NO_CHOICES[0])

        if not user_want_to_scrap:
            break
