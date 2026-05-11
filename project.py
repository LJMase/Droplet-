class Project():
    def __init__(self, category, name, description="", minis={}):
        self.category = category 
        self.name = name 
        self.description = description
        self.minis = minis
        self.__mini_num = 1

    # Because the mini object is mutable there's no good way to use it as a key. However, we'll only access the data through for loops, so we can just use an iterating num as the key. 
    def add_mini(self, mini, amount):
        self.minis[self.__mini_num] = {"Mini": str(mini), "Amount": amount, "Paints": ""}
        self.minis[self.__mini_num]["Status"] = {"On-Sprue": amount, "Assembled": 0, "Primed": 0, "Painted": 0}
        self.__mini_num += 1

    def print_mini(self, mini_num):
        return f"{self.minis[mini_num]}"

    def __eq__(self, other):
        return self.name == other.name and self.category == other.category

    def __str__(self):
        return f"({self.category}) {self.name}: {self.description}"

    def __lt__(self, other):
        if self.name == other.name:
            return self.category < other.category
        return self.name < other.name    