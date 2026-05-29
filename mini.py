class Mini():
    def __init__(self, game: str, faction: str, name: str):
        self.game = game 
        self.faction = faction
        self.name = name 

    # Dunder equals is used for finding equivalent mini objects when I compare them in main.
    def __eq__(self, other):
        return self.name == other.name and self.faction == other.faction and self.game == other.game

    # Dunder str is used to provide a custom print format for the mini objects.
    def __str__(self):
        return f"{self.name} - {self.faction} ({self.game})"

    # Dunder less than compares objects alphabetically based on game and then faction. This is primarily to use sorted() on a list of minis.
    def __lt__(self, other): 
        if self.game == other.game:
            return self.faction < other.faction 
        return self.game < other.game