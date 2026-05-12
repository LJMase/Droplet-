class Project():
    def __init__(self, category, name, description="", minis={}):
        self.category = category 
        self.name = name 
        self.description = description
        self.minis = minis
        self.__mini_num = 1

    # Because the mini object is mutable there's no good way to use it as a key. However, we'll only access the data through for loops, so we can just use an iterating num as the key. 
    def add_mini(self, mini, amount):
        for key in self.minis:
            if mini == self.minis[key]["Mini"]:
                print("Mini already added.")
        self.minis[self.__mini_num] = {"Mini": str(mini), "Amount": amount, "Paints": ""}
        self.minis[self.__mini_num]["Status"] = {"On-Sprue": amount, "Assembled": 0, "Primed": 0, "Painted": 0}
        self.__mini_num += 1

    def change_mini_status(self, mini, status, amount):
        total_status = 0
        for key, value in self.minis[mini]["Status"].items():
            total_status += value
        if total_status < amount:
            print("Not enough miniatures!")
            return 0
        for key, value in self.minis[mini]["Status"].items():
            if key == status:
                continue 
            if not amount - value < 0:
                self.minis[mini]["Status"][status] += value
                amount -= value 
                self.minis[mini]["Status"][key] = 0
            else:
                self.minis[mini]["Status"][key] -= amount 
                self.minis[mini]["Status"][status] += amount
                amount = 0
    
    def change_mini_amount(self, mini, amount):
        total_minis = 0
        if amount == 0:
            print("Amount set to 0, deleting mini.")
            del self.minis[mini]
        elif amount < self.minis[mini]["Amount"]:
            self.minis[mini]["Amount"] = amount 
            for key in self.minis[mini]["Status"]:
                self.minis[mini]["Status"][key] = 0
            self.minis[mini]["Status"]["On-Sprue"] = amount
        else:
            self.minis[mini]["Amount"] = amount 
            for key, value in self.minis[mini]["Status"].items():
                total_minis += value
            self.minis[mini]["Status"]["On-Sprue"] += amount - total_minis

    def print_minis(self):
        for key, value in self.minis.items():
            print(f"{self.minis[key]["Amount"]}x {self.minis[key]["Mini"]}: {self.minis[key]["Status"]["On-Sprue"]} On-Sprue, {self.minis[key]["Status"]["Assembled"]} Assembled, {self.minis[key]["Status"]["Primed"]} Primed, {self.minis[key]["Status"]["Painted"]} Painted. Paint Scheme: {self.minis[key]["Paints"]}")

    def __eq__(self, other):
        return self.name == other.name and self.category == other.category

    def __str__(self):
        return f"({self.category}) {self.name}: {self.description}"

    def __lt__(self, other):
        if self.name == other.name:
            return self.category < other.category
        return self.name < other.name    