import csv

dict_of_values = {"1": "d", "2": 3,  "3": ["1", "2"]}


def dict_to_csv(filename):
    with open(filename, 'w') as file:
        output_file = csv.writer(file, delimiter="\t")
        for key in list(dict_of_values):
            output_file.writerow((key, dict_of_values.get(key), type(dict_of_values.get(key))))


dict_to_csv("exercise22_beyond2__support_file.csv")
