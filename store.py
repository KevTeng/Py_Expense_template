import csv


FILE_CSV_NAME = 'expense_report.csv'
DICO_NAME_LABEL = {}
DICO_NAME_SPENDER = {}

def write_in_csv( amount: int, label: str, actor: str, spender: str):
    with open(FILE_CSV_NAME, 'a', newline='\n') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        spamwriter.writerow([amount, label, actor, spender])
    print('Writing ended')

def display_csv():
    with open(FILE_CSV_NAME, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))



#
# if __name__ == "__main__":
#     write_in_csv(12, 'voyage', 'toto')
#     write_in_csv(20, 'grec', 'toto')
#     write_in_csv(8, 'mcdo', 'toto')
#     display_csv()