class Mini():
    def __init__(self, game: str, faction: str, name: str):
        self.game = game 
        self.faction = faction
        self.name = name 

    def __eq__(self, other):
        return self.name == other.name and self.get_faction() == other.get_faction() and self.get_game() == other.get_game()

    def __str__(self):
        return f"{self.name} - {self.faction} ({self.game})"

    def __lt__(self, other):
        if self.game == other.game:
            return self.faction < other.faction 
        return self.game < other.game