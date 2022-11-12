from io import StringIO

string = 'This is a string.'
file1 = StringIO(string)

file2 = open("exercise9_beyond3_support_file.txt")


def largest_word_check(file):
    list_of_words = (file.read()).split(" ")
    largest_word = list_of_words[1]
    for i in range(len(list_of_words)):
        if len(largest_word) < len(list_of_words[i]):
            largest_word = list_of_words[i]
        else:
            pass

    print(largest_word)


largest_word_check(file2)
