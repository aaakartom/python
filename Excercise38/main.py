from Beverage import *

def output_beverage():
    for item in [Beverage(beverage, temperature)
                 for beverage, temperature
                 in {"Bloody Mary": 20, "Water": 10, "Coke": 10}.items()]:
        print(item)


output_beverage()
