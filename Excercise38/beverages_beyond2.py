class Beverage():
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

        if temperature == None:
            self.temperature = 75

    def __repr__(self):
        return self.name + " " + str(self.temperature) + "C"