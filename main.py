from expense import new_expense, pretty_printer_of_status

from user_manager import *



def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()
    if (option['main_options']) == "New User":
        new_user()
        ask_option()
    if (option['main_options']) == "Show Status":
        pretty_printer_of_status()
        ask_option()

def main():
    ask_option()

main()
