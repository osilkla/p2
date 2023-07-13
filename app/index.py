import os
from services.display_choices_menu import (
    display_extract_all_or_category_menu_to_user,
    display_extract_one_category_menu_to_user,
    display_continue_or_quit_menu,
    USER_CHOICE_SCRAP_ALL,
    USER_CHOICE_SCRAP_CAT,
    USER_YES_CHOICE,
    USER_CHOICE_SCRAP_ALL_FROM_SELECTED_CAT,
)
from services.book_scraper import (
    get_categories_list,
    save_books_in_csv,
)
from services.utils import init_directory, remove_items_from_dict
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

        user_want_to_scrap = bool(user_choice == USER_YES_CHOICE)

        if not user_want_to_scrap:
            break

# In case off partial failed "SCRAP_ALL" the user might want to complete the unscrapped category
elif user_choice == USER_CHOICE_SCRAP_ALL_FROM_SELECTED_CAT:
    user_category_url, category_name = display_extract_one_category_menu_to_user(
        categories
    )
    list_to_scrap = remove_items_from_dict(categories, category_name)
    for category, url in list_to_scrap.items():
        save_books_in_csv(url, category)
