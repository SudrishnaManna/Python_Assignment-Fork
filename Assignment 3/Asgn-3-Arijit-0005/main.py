class Unique:
    def __init__(self):
        self.hash = {}
    
    def count_unique(self, text):
        words = text.split()
        for i in words:
            if i not in self.hash:
                self.hash[i] = 1
            else:
                self.hash[i] += 1
        return self.hash

    def print_unique(self):
        with open("Assignment_3/Asgn-3-Arijit-0005/raw_data.txt", "r") as file:
            f = file.read()
            print(self.count_unique(f))

u = Unique()
u.print_unique()