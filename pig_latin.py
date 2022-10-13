your_input = input()


list_of_vowels = ["a", "e", "i", "o", "u"]

for i in range(len(your_input)):
    if your_input[0] in list_of_vowels:
        output = str(your_input) + "way"

    else:
        your_input_list = list(your_input)
        your_input_list_2 = your_input_list + [your_input_list[0]]
        your_input_list_2.pop(0)
        output = ''.join(your_input_list_2 + ['a','y'])


print(output)

