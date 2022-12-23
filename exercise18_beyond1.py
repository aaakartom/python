with open("exercise18_beyond1__support_file.txt", "r") as txt_file:
    for line in txt_file:
        file_list = line.split(' ')
        sum_of_integers = 0
        for word in file_list:
            if word.isnumeric():
                sum_of_integers += int(word)

        print(sum_of_integers)
