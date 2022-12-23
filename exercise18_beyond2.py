
with open("exercise18_beyond2__support_file.txt") as txt_file:
    product = 0
    for line in txt_file:
        numbers = line.split("\t")
        if len(numbers) > 1:
            number1 = numbers[0].strip()
            number2 = numbers[1].strip()
            if number1.isnumeric() and number2.isnumeric():
                product += int(number1) * int(number2)

    print(product)






