class Project():
    def __init__(self, category, name, description="", minis=[]):
        self.category = category 
        self.name = name 
        self.description = description
        self.minis = {}

    def add_mini(self, mini):
        self.minis[str(mini)] = {"Amount": 0, "Paints": ""}
        self.minis[str(mini)]["Status"] = {"On-Sprue": 0, "Assembled": 0, "Primed": 0, "Painted": 0}

    def __eq__(self, other):
        return self.name == other.name and self.category == other.category

    def __str__(self):
        return f"({self.category}) {self.name}: {self.description}"

    def __lt__(self, other):
        if self.name == other.name:
            return self.category < other.category
        return self.name < other.name    