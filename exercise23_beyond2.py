import json 
import csv


def password_to_json(password_filename, json_filename):
    with open(password_filename) as password, open(json_filename, 'w') as output:
        input_file = csv.reader(password, delimiter=":")

        list_of_dicts = []
        for record in input_file:
            if len(record) > 1:
                dictionary = {}
                for i in range(len(record)):
                    dictionary[i] = record[i]
                list_of_dicts.append(dictionary)

        json_object = json.dumps(list_of_dicts)
        output.write(json_object)


password_to_json("exercise23_beyond2__support_file1.csv", "exercise23_beyond2__support_file2.json")
