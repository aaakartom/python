sequence = (10, 20, 'a', '30', 'bcd')

def mysum_bigger_than(*args):
    initial_sum = 0
    for item in sequence[0:]:
        if type(item) == str:
            if item.isnumeric() == True:
                initial_sum += int(item)
            else:
                pass
        else:
            initial_sum += item


    print(initial_sum)

mysum_bigger_than(sequence)