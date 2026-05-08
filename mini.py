class Mini():
    def __init__(self, game, faction, name):
        self.game = game 
        self.faction = faction
        self.name = name 
        self.__status = "on sprue"

    def change_status(status):
        self.__status = status 

    def __eq__(self, other):
        if self.name == other.name and self.get_faction() == other.get_faction() and self.get_game() == other.get_game():
            return True
        return False 

    def __str__(self):
        return f"{self.name} - {self.faction} ({self.game})"

    def __lt__(self, other):
        if self.game == other.game:
            return self.faction < other.faction 
        return self.game < other.game