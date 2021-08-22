class Get:
    def __init__(self, path, create = False):
        self.path = path
        if create != True:
            self.read_file = open(self.path, "r")
            self.add_file = open(self.path, "a")
        elif create == True:
            self.write_file = open(self.path, "w")
            self.write_file.close()
            self.read_file = open(self.path, "r")
            self.add_file = open(self.path, "a")

    def save(self):
        self.add_file.close()
        self.read_file.close()

    def overlap(self, string = ""):
        self.string = string
        self.write_file = open(self.path, "w")
        self.write_file.write(self.string)
        self.write_file.close()

    def add(self, string = ""):
        self.string = string
        self.add_file.write(self.string)

    def read(self):
        self.data = self.read_file.readlines()
        for self.i in range(0, len(self.data), 1):
            self.data[self.i] = self.data[self.i].removesuffix("\n")
        return self.data
