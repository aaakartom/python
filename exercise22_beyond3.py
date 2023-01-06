import csv
import random


def write_csv_file(filename):
    with open(filename, 'w') as file:
        csv_file = csv.writer(file, delimiter="\t")

        for i in range(3):
            set_of_numbers = ()

            for x in range(10):

                set_of_numbers = set_of_numbers + (random.randint(10, 100), )

            csv_file.writerow(set_of_numbers)


def sum_and_mean(filename):
    with open(filename, 'r') as file:
        csv_file = csv.reader(file, delimiter="\t")

        for line in csv_file:
            sum_of_numbers = 0
            if len(line) > 1:
                for number in line:
                    sum_of_numbers += int(number)

                print(f"Sum of numbers: {sum_of_numbers}")
                print(f"Mean of numbers: {sum_of_numbers/10}")


write_csv_file("exercise22_beyond3__support_file.csv")
sum_and_mean("exercise22_beyond3__support_file.csv")
