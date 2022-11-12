import datetime as dt

dates_of_births = {'Sergey': dt.date(1971, 5, 13), 'Tatyana': dt.date(1972, 10, 13), 'Artyom': dt.date(2005, 10, 20)}
today = dt.date.today()

user_input = input("Enter the name:")

date_of_births2 = dates_of_births.get(user_input)
print(today-date_of_births2)
