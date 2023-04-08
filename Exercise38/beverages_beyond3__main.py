class LogFile():
    def __init__(self, name):
        self.log_file = open(name, "w")

    def write(self, text):
        self.log_file.write(text)
        self.log_file.write("\n")

if __name__ == "main":
    log = LogFile("beverages_beyond3__file.txt")
    log.write("Here I am writing some text into my log.")
    log.write("... and a little bit more")
