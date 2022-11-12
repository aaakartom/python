list_tuple_string = [1888, 9, 4, 5]


def largest(sequence):
    largest_value = sequence[1]
    for i in range(len(sequence)):
        if float(largest_value) < float(sequence[i]):
            largest_value = float(sequence[i])
        else:
            pass

    print(largest_value)


largest(list_tuple_string)
