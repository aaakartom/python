dict_of_vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

with open("exercise18_beyond3__support_file.txt", "r") as txt_file:
    for line in txt_file:
        for character in line:
            if character in dict_of_vowels.keys():
                dict_of_vowels[character] += 1

    print(dict_of_vowels)
