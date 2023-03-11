class Beverage():
    def __init__(self, name, temperature=75):
        self.name = name
        self.temperature = temperature

    def __repr__(self):
        return self.name + " " + str(self.temperature) + "C"