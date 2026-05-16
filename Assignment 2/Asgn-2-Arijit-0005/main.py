class Unique:
    def __init__(self):
        self.hash = {}
    
    def remove_duplicates(self, list):
        for i in list:
            if i not in self.hash:
                self.hash[i] = 1
            else:
                self.hash[i] += 1
        return [key for key in self.hash.keys()]

l = list(
    map(
        lambda x: int(x), 
        input("Enter the list: ").split(" ")
    )
)

u = Unique()
print(u.remove_duplicates(l))