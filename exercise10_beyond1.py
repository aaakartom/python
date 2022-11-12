sequence = [10, 5, 20, 30, 6]
limit = 10

def mysum_bigger_than(*args):
    initial_sum = 0
    for item in sequence[0:]:
        if limit >= item:
            pass
        else:
            initial_sum += item

    print(initial_sum)

mysum_bigger_than(limit, sequence)