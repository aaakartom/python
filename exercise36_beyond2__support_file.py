def true_characters(string):
    str_list = list(string)
    number_of_isdigit = len([character for character in str_list if character.isdigit()])
    number_of_isalpha = len([character for character in str_list if character.isalpha()])
    number_of_isspace = len([character for character in str_list if character.isspace()])

    print({"isdigit": number_of_isdigit, "isalpha": number_of_isalpha, "isspace": number_of_isspace})
