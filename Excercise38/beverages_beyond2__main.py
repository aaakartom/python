from beverages_beyond2 import *

def output_beverage():
    beverages = [Beverage(beverage, temperature)
                 for beverage, temperature
                 in {"Bloody Mary": 20, "Coke": 10}.items()]
    beverages.append(Beverage('Water'))

    for item in beverages:
        print(item)


output_beverage()

