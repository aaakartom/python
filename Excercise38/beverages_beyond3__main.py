class LogFile():
    def __init__(self, name):
        self.name = open(name, "r+")

    def write(self):
        self.name.write("Text")

    def read(self):
        print(self.name.read())



LogFile.write(LogFile("beverages_beyond3__file.txt"))
LogFile.read(LogFile("beverages_beyond3__file.txt"))