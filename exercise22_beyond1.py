import csv

user_input_list_of_integers = input()
list_of_integers = user_input_list_of_integers.split(" ")

user_input_delimiter = input()


def password_to_csv(password_filename, csv_filename):
    with open(password_filename) as password, open(csv_filename, 'w') as output:
        input_file = csv.reader(password, delimiter=":")
        output_file = csv.writer(output, delimiter=user_input_delimiter)

        for record in input_file:
            if len(record) > 1:
                output_file.writerow((record[int(list_of_integers[0])], record[int(list_of_integers[1])]))


password_to_csv("exercise22_beyond1__support_file1.csv", "exercise22_beyond1__support_file2.csv")
