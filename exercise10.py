def mysum(*items):
    if not items:
        return items

    initial_sum = items[0]

    for item in items[1:]:
        initial_sum += item

    return initial_sum


print(mysum((1, 2, 3),(1, 2, 3)))


for item in [[],[],[],[],[],[]]:
    if item == 9:
        do somth



d = {'Warminster': 5, 'New York': 7, 'Philadelphia': 4, ....}

for item in d.items():
    item[0]
    item[1]

sum = 0
length = len(d)
for key, value in d.items():
    sum += value

average = sum/length

students = {
            '6378462': {'name': 'John Doe', 'age': 15, 'email': 'jdoe@example.com', 'height': 5.6},
            '3784672': {'name': 'Joan Doe', 'age': 40, 'email': 'jadoe@example.com', 'height': 4.0},
            '7358263': {'name': 'Serge Muzyka', 'age': 41, 'email': 'muzyka@example.com', 'height': 5.8}
            }
students['7358263']['age'] = 14

s = students['7358263']
s['age'] = 14

females = {'3784672'}

