from mini import Mini 
from project import Project 
from paint import Paint 

miniatures = ["Termagant", "Terminator", "Titus", "Calgar", "Tyrannofex", "Ripper Swarm", "Mortarion", "Norn Emissary", "Ghazghull"]
paints = ["Ultramarine Blue", "Mephiston Red", "Wraithbone", "Guilliman Flesh", "Corax White", "Abaddon Black", "Thunderhawk Blue"]

def display_menu():
    try:
        choice = int(input("Welcome to Droplet! What would you like to do?\n1. Open a Project\n2. Change Miniatures\n3. Change Paints\n4. Exit\n"))
    except ValueError:
        print("\nWARNING: Must be a number 1-4.\n")
        display_menu()
        
    match choice:
        case 1:
            pass
        case 2:
            print(f"\nHere are the most recent Miniatures: ")
            for i in range(1, 6):
                print(f"{i}. {miniatures[-i]}")
            print("\nWhat would you like to do?\n1. Add a Mini\n2. Edit a Mini\n3. Delete a Mini")
        case 3:
            return f"\nHere are the most recent Paints:\n{paints[-5:]}"
        case 4:
            return 0 
        case _:
            print("\nWARNING: Must be a number 1-4.\n")
            display_menu()

def main():
    display_menu()

main()