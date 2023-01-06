def longest_word_function(filename):
    with open(filename, 'r') as file:
        file_contents = file.read()
        words = file_contents.split(" ")

        longest_word = words[0]
        for word in words:
            if len(longest_word) < len(word):
                longest_word = word

        return longest_word


txt_files = ["exercise21__support_file1.txt", "exercise21__support_file2.txt", "exercise21__support_file3.txt"]

files_with_longest_words = {}

for txt_file in txt_files:
    files_with_longest_words[longest_word_function(txt_file)] = txt_file

print(files_with_longest_words)