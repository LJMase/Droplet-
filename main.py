import os
from mini import Mini 
from project import Project 
from paint import Paint 

mini_csv, paint_csv = "./miniatures.csv", "./paints.csv"
miniatures = []
paints = ["Ultramarine Blue", "Mephiston Red", "Wraithbone", "Guilliman Flesh", "Corax White", "Abaddon Black", "Thunderhawk Blue"]

def load_objects():
    if os.path.isfile(mini_csv):
        with open(mini_csv, "r") as file:
            for line in file:
                words = [word.strip() for word in line.split(",")]
                miniatures.append(Mini(words[0], words[1], words[2]))
    else:
        with open(mini_csv, "w"):
            pass 

    if os.path.isfile(paint_csv):  
        with open(paint_csv, "r") as file:
            for line in file:
                pass
    else:
        with open(paint_csv, "w"):
            pass 

def display_main_menu():
    while True:
        try:
            choice = int(input("\nWelcome to Droplet! What would you like to do?\n1. Open a Project\n2. Change Miniatures\n3. Change Paints\n4. Exit\n"))
        except ValueError:
            print("\nWARNING: Must be a number 1-4.\n")
            continue
            
        match choice:
            case 1:
                pass
            case 2:
                display_miniatures_menu()
                return 0
            case 3:
                return f"\nHere are the most recent Paints:\n{paints[-5:]}"
            case 4:
                with open(mini_csv, "w") as file:
                    for mini in miniatures:
                        file.write(f"{mini.game}, {mini.faction}, {mini.name}\n")

                with open(paint_csv, "w") as file:
                    for paint in paints:
                        #file.write(f"{paint.get_brand()}, {paint.get_color()}, {paint.get_sku()}\n")
                        pass
                return 0 
            case _:
                print("\nWARNING: Must be a number 1-4.\n")

def display_miniatures_menu():
    while True:
        try:
            choice = int(input("What would you like to do?\n1. Add a Mini\n2. Edit a Mini\n3. Delete a Mini\n4. View Miniatures\n5. Go Back\n"))
        except ValueError:
            print("\nWARNING: Must be a number 1-3.\n")
        
        match choice:
            case 1:
                print("\nPlease enter the game(40k, D&D, etc.), the faction, and the name of the miniature.")
                miniatures.append(Mini(input("Game: "), input("Faction: "), input("Name: "))) 
            case 2:
                print("\nEnter the details of the miniature you would like to edit: ")
                game, faction, name = input("Game: "), input("Faction: "), input("Name: ")
                for mini in miniatures: 
                    if mini == Mini(game, faction, name):
                        print("\nMini Found! Enter the new details below:")
                        new_game, new_faction, new_name = input("New Game: "), input("New Faction: "), input("New Name: ")
                        mini.game, mini.faction, mini.name = new_game, new_faction, new_name
                        break 
                    # Using else here would print the not found result every for loop and putting it outside the for loop results in it running every time. This is my solution. 
                    if mini == miniatures[len(miniatures)-1]:
                        print("Mini Not Found")
            case 3:
                print("\nEnter the details of the miniature you would like to delete:")
                game, faction, name = input("Game: "), input("Faction: "), input("Name: ")
                for mini in miniatures:
                    if mini == Mini(game, faction, name):
                        print("\nMini Deleted!")
                        miniatures.remove(mini)
                        break
                    if mini == miniatures[len(miniatures)-1]:
                        print("Mini Not Found")
            case 4:
                for i in range(0, len(miniatures)):
                    print(f"{i+1}: {sorted(miniatures)[i]}")
            case 5:
                display_main_menu()
                return 0
            case _:
                print("\nWARNING: Must be a number 1-3.\n")

def main():
    load_objects()
    display_main_menu()

main()