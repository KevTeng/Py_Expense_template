from store import *
from user_manager import *
from PyInquirer import *

FILE_CSV_NAME = 'expense_report.csv'


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",

    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"checkbox",
        "name":"actor",
        "message":"Actors who didn't pay - actor: ",
        "choices": display_list_of_user(),
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": display_real_list_of_user(),
    },

]

def csv_to_list():
    res = []
    with open(FILE_CSV_NAME, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        res = list(spamreader)
    # res[0] = int(res[0])
    # res[2] = list(res[2])
    # print(res)
    return res


def count_user_total(liste: str):
    return liste.count(',') + 2

def have_dept(liste, name):
    if name in liste[2]:
        return True
    return False

def get_dept(name: str, spender: str):
    liste = (csv_to_list())
    dept = 0
    for i in range(len(liste)):
        if have_dept(liste[i], name) and liste[i][3] == spender:
            # print(int(liste[i][0]))
            dept += int(liste[i][0]) / count_user_total(liste[i][2])
    return dept



def new_expense(*args):

    infos = prompt(expense_questions)
    # if infos['spender']:
    #     print('go')
    # print(infos)
    int(infos['amount'])
    write_in_csv(infos['amount'], infos['label'], infos['actor'], infos['spender'])
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True

def pretty_printer_of_status():
    liste_of_user = display_real_list_of_user()

    for user in liste_of_user:
        printed = False
        for user2 in liste_of_user:
            if get_dept(user, user2) != 0:
                print(f"{user} owes {get_dept(user, user2)}€ to {user2}")
                printed = True
        if not printed:
            print(f"{user} owes nothing")

# if __name__ == "__main__":
#
#     print((get_dept("Kev", "SIGL")))

