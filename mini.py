class Mini():
    def __init__(self, game, faction, name):
        self.__game = game 
        self.__faction = faction
        self.name = name 
        self.__status = "on sprue"

    def change_status(status):
        self.__status = status 

    def get_game():
        return self.__game
    
    def get_faction():
        return self.__faction 