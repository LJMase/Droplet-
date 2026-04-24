class Mini():
    def __init__(self, game, faction, name):
        self.__game = game 
        self.__faction = faction
        self.name = name 
        self.__status = "on sprue"

    def change_status(status):
        self.__status = status 
    
    def __str__(self):
        return f"{self.name} - {self.__faction} ({self.__game})"

    def get_game(self):
        return self.__game
    
    def get_faction(self):
        return self.__faction 