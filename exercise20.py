def wordcount():
    with open("exercise20__support_file.txt", "r") as txt_file:
        file_contents = txt_file.read()
        print(f"Number of characters: {len(file_contents)}")
        words = file_contents.split()
        print(f"Number of words: {len(words)}")
        lines = file_contents.split("\n")
        print(f"Number of lines: {len(lines)}")
        copy_of_words = file_contents.split()
        number_of_unique_words = 0
        for word in words:
            copy_of_words.remove(word)
            if word not in copy_of_words:
                number_of_unique_words += 1
        print(f"Number of unique words: {number_of_unique_words}")


wordcount()
