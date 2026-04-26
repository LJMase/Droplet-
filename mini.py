class Mini():
    def __init__(self, game, faction, name):
        self.__game = game 
        self.__faction = faction
        self.name = name 
        self.__status = "on sprue"

    def change_status(status):
        self.__status = status 

    def __eq__(self, other):
        if self.name == other.name and self.get_faction() == other.get_faction() and self.get_game() == other.get_game():
            return True
        return False 

    def __str__(self):
        return f"{self.name} - {self.__faction} ({self.__game})"

    def get_game(self):
        return self.__game
    
    def get_faction(self):
        return self.__faction 