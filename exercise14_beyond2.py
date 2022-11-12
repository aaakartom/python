database_temperatures = {'11/11': '16.5 C', '11/12': '16 C', '11/13': '7.5 C',
                         '11/14': '4 C', '11/15': '2.5 C', '11/16': '7 C', '11/17': '3.5 C'
                         }

dates = list(database_temperatures.keys())

user_date = input('Enter date:')
temperature = database_temperatures.get(user_date)
if temperature:
    index = dates.index(user_date)
    print(f"Current temperature: {temperature}")

    if index - 1 >= 0:
        prev_date = dates[index - 1]
        print(f'Previous temperature: {database_temperatures.get(prev_date)}')
    if index + 1 < len(dates):
        next_date = dates[index + 1]
        print(f'Next temperature: {database_temperatures.get(next_date)}')
else:
    print("That date was not tracked.")
