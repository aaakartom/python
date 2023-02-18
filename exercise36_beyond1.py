income = int(input())
tax_percentage = 0


def calculate_tax(income_value):
    global tax_percentage

    if 1000 <= income_value < 11000:
        tax_percentage = 10

    elif 11000 <= income_value < 21000:
        tax_percentage = 20

    elif income_value >= 21000:
        tax_percentage = 50

    tax = income * (tax_percentage/100)

    return tax


print(calculate_tax(income))
