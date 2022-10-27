def mysum(*items):
    if not items:
        return items

    initial_sum = items[0]

    for item in items[1:]:
        initial_sum += item

    return initial_sum


print(mysum((1, 2, 3),(1, 2, 3)))
