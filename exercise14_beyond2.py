database_temperatures = {'11/11': '16.5 C', '11/12': '16 C', '11/13': '7.5 C',
                         '11/14': '4 C', '11/15': '2.5 C', '11/16': '7 C', '11/17': '3.5 C'
                         }


user_date = input('Enter date:')


temperature = database_temperatures.get(user_date)

print(f"Current temperature: {temperature}")
for i in range(len(list(database_temperatures))):
    if list(database_temperatures)[i] == user_date:
        a = i-1
        b = i+1

        if a > 0:
            print(f'Previous temperature: {database_temperatures.get(list(database_temperatures)[a])}')
        elif b < (len(list(database_temperatures)))-1:
            print(f'Next temperature: {database_temperatures.get(list(database_temperatures)[b])}')

