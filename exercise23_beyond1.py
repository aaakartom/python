import csv
import json


def password_to_json(password_filename, json_filename):
    with open(password_filename) as password, open(json_filename, 'w') as output:
        input_file = csv.reader(password, delimiter=":")

        list_of_tuples = []
        for record in input_file:
            if len(record) > 1:
                line_tuple = ()
                for field in record:
                    line_tuple = line_tuple + (field, )
                list_of_tuples.append(line_tuple)
            print(list_of_tuples)
            json_object = json.dumps(list_of_tuples)
        output.write(json_object)


password_to_json("exercise23_beyond1__support_file1.csv", "exercise23_beyond1__support_file2.json")
