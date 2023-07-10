import inquirer
from const import USER_CHOICES, USER_YES_NO_CHOICES


def display_extract_all_or_category_menu_to_user() -> str:
    print("What do you want to do ?")
    user_choice = input(
        "Type 'All' if you want to srap all books, Type 'Category' if you want to scrap only one Category: "
    ).upper()
    if user_choice not in USER_CHOICES:
        print("This input is not a valid choice: ", user_choice)
    else:
        return user_choice


def display_extract_one_category_menu_to_user(categories: dict):
    category_question = [
        inquirer.List(
            "category",
            message="What category do you want to extract?",
            choices=categories.keys(),
        ),
    ]
    category_name = inquirer.prompt(category_question)["category"]
    user_category_url = categories[category_name]
    return user_category_url, category_name


def display_continue_or_quit_menu() -> str:
    continue_or_quit_question = [
        inquirer.List(
            "continue",
            message="Do you want to extract an other one?",
            choices=USER_YES_NO_CHOICES,
        ),
    ]
    user_choice = inquirer.prompt(continue_or_quit_question)["continue"]
    return user_choice
