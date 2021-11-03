from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"Username",
        "message":"New user - Name: ",
    }
]

USER_CSV = 'users.csv'

def store_user(username: str):
    with open(USER_CSV, 'a', newline='\n') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        spamwriter.writerow([username])

def display_list_of_user():
    my_list = []
    with open(USER_CSV, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            my_list.append({'name' : row[0]})
    return my_list

def display_real_list_of_user():
    my_list = []
    with open(USER_CSV, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            my_list.append(row[0])
    return my_list


def new_user(*args):
    infos = prompt(user_questions)
    store_user(infos['Username'])
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print(f"{infos['Username']} Added !")
    return True


if __name__ == "__main__":
    store_user("Kev")
    print(display_list_of_user())