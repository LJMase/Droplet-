class Project():
    def __init__(self, category, name, description):
        self.__category = category 
        self.__name = name 
        self.__description = description
        self.minis = []

    def add_mini(mini):
        self.minis.append(mini)
    
    def get_category():
        return self.__category
    
    def get_name():
        return self.__name
    
    def get_description():
        return self.__description
