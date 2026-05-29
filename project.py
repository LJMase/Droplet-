from mini import Mini

class Project():
    def __init__(self, category: str, name: str, description="", minis={}):
        self.category = category 
        self.name = name 
        self.description = description
        self.minis = minis
        if self.minis:
            self.__mini_num = int(next(reversed(self.minis)))+1
        else:
            self.__mini_num = 1

    # Because the mini object is mutable there's no good way to use it as a key. However, we'll only access the data through for loops, so we can just use an iterating num as the key. 
    def add_mini(self, mini: Mini, amount: int) -> None | int:
        for key in self.minis:
            if str(mini) == self.minis[key]["Mini"]:
                print("Mini already added.")
                return 0
        self.minis[str(self.__mini_num)] = {"Mini": str(mini), "Amount": amount, "Paints": ""}
        self.minis[str(self.__mini_num)]["Status"] = {"On-Sprue": amount, "Assembled": 0, "Primed": 0, "Painted": 0}
        self.__mini_num += 1

    def change_mini_status(self, mini: int, status: str, amount: int) -> None | int:
        total_status = 0
        for value in self.minis[mini]["Status"].values():
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
    
    def change_mini_amount(self, mini: int, amount: int) -> None:
        total_minis = 0
        if amount == 0:
            print("Amount set to 0, deleting mini.")
            self.delete_mini(mini)
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

    def delete_mini(self, mini: int) -> None:
        temp_minis = {}
        temp_key = 1
        del self.minis[mini]
        for key in self.minis:
            temp_minis[str(temp_key)] = self.minis[key]
            temp_key += 1
        self.minis = temp_minis

    def print_minis(self) -> None:
        print("\n--------Project Miniatures--------")
        for key, value in self.minis.items():
            print(f"{self.minis[key]["Amount"]}x {self.minis[key]["Mini"]}: {self.minis[key]["Status"]["On-Sprue"]} On-Sprue, {self.minis[key]["Status"]["Assembled"]} Assembled, {self.minis[key]["Status"]["Primed"]} Primed, {self.minis[key]["Status"]["Painted"]} Painted. Paint Scheme: {self.minis[key]["Paints"]}")
        print("----------------------------------")

    # Dunder equals is used for finding equivalent project objects when I compare them in main.
    def __eq__(self, other):
        return self.name == other.name and self.category == other.category

    # Dunder str is used to provide a custom print format for the project objects. If the SKU is 0 it will not be included in the print. 
    def __str__(self):
        return f"({self.category}) {self.name}: {self.description}"

    # Dunder less than compares objects alphabetically based on name and then category. This is primarily to use sorted() on a list of projects.
    def __lt__(self, other):
        if self.name == other.name:
            return self.category < other.category
        return self.name < other.name    