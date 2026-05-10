import os
import json
from mini import Mini 
from project import Project 
from paint import Paint 

mini_csv, paint_csv, project_csv = "./miniatures.csv", "./paints.csv", "./projects.csv"
miniatures = []
paints = []
projects = []

def load_objects():
    if os.path.isfile(mini_csv):
        with open(mini_csv, "r") as file:
            for line in file:
                words = [word.strip() for word in line.split(",")]
                miniatures.append(Mini(words[0], words[1], words[2]))
    else:
        print("No miniatures file found. Creating new file...")
        with open(mini_csv, "w"):
            pass 

    if os.path.isfile(paint_csv):  
        with open(paint_csv, "r") as file:
            for line in file:
                words = [word.strip() for word in line.split(",")]
                paints.append(Paint(words[0], words[1], words[2]))
    else:
        print("No paint file found. Creating new file...")
        with open(paint_csv, "w"):
            pass 
    
    if os.path.isfile(project_csv):  
        with open(project_csv, "r") as file:
            for line in file:
                words = [word.strip() for word in line.split(",")]
                projects.append(Project(words[0], words[1], words[2], words[3]))
    else:
        print("No project file found. Creating new file...")
        with open(project_csv, "w"):
            pass 

def display_main_menu():
    while True:
        try:
            choice = int(input("\nWelcome to Droplet! What would you like to do?\n1. Open a Project\n2. Create a Project\n3. View All Projects\n4. Change Miniatures\n5. Change Paints\n6. Exit\n"))
        except ValueError:
            print("\nWARNING: Must be a number 1-6.\n")
            continue
            
        match choice:
            case 1:
                print("Please enter the project name and category: ")
                project_name, project_category = input("Name: "), input("Category: ")
                for project in projects:
                    if project == Project(project_name, project_category):
                        display_projects_menu(project)
                        return 0
                    if project == projects[len(projects)-1]:
                        print("Project not found.")    
            case 2:
                print("Enter the project category, name, and description.")
                project_category, project_name, project_description = input("Category: "), input("Name: "), input("Description: ")
                projects.append(Project(project_category, project_name, project_description))
            case 3:
                for i in range(0, len(projects)):
                    print(f"{i+1}. {sorted(projects)[i]}")
            case 4:
                display_miniatures_menu()
                return 0
            case 5:
                display_paints_menu()
                return 0
            case 6:
                with open(mini_csv, "w") as file:
                    for mini in miniatures:
                        json.dump(f"{mini.game}, {mini.faction}, {mini.name}", file)

                with open(paint_csv, "w") as file:
                    for paint in paints:
                        json.dump(f"{paint.brand}, {paint.color}, {paint.sku}", file)

                with open(project_csv, "w") as file:
                    for project in projects:
                        json.dump(f"{project.category}, {project.name}, {project.description}, {project.minis}", file)

                return 0 
            case _:
                print("\nWARNING: Must be a number 1-6.")

def display_projects_menu(project):
    while True:
        try:
            choice = int(input("\n1. Add a Mini\n2. View Minis\n3. Paint a Mini\n4. Change Mini Status\n5. Change Project Status\n6. Exit\n"))
        except ValueError:
            print("\nWARNING: Must be a number 1-6.\n")
            continue

        match choice:
            case 1:
                project.add_mini(miniatures[1])
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass 
            case 5:
                pass
            case 6:
                display_main_menu()
                return 0
            case _:
                print("\nWARNING: Must be a number 1-6.\n") 

def display_miniatures_menu():
    while True:
        try:
            choice = int(input("What would you like to do?\n1. Add a Mini\n2. Edit a Mini\n3. Delete a Mini\n4. View Miniatures\n5. Go Back\n"))
        except ValueError:
            print("\nWARNING: Must be a number 1-5.\n")
        
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
                print("\nWARNING: Must be a number 1-5.\n")

def display_paints_menu():
    while True:
        try:
            choice = int(input("What would you like to do?\n1. Add a Paint\n2. Edit a Paint\n3. Delete a Paint\n4. View Paints\n5. Go Back\n"))
        except ValueError:
            print("\nWARNING: Must be a number 1-5.\n")

        match choice:
            case 1:
                print("\nPlease enter the name, the brand, and the SKU (if N/A, enter 0).")
                paints.append(Paint(input("Brand: "), input("Color: "), input("SKU: "))) 
            case 2:
                print("\nEnter the details of the paint you would like to edit: ")
                brand, color, sku = input("Brand: "), input("Color: "), input("SKU (0 for none): ")
                for paint in paints: 
                    if paint == Paint(brand, color, sku):
                        print("\nPaint Found! Enter the new details below:")
                        new_brand, new_color, new_sku = input("New Brand: "), input("New Color: "), input("New SKU: ")
                        paint.brand, paint.color, paint.sku = new_brand, new_color, new_sku
                        break 
                    # Using else here would print the not found result every for loop and putting it outside the for loop results in it running every time. This is my solution. 
                    if paint == paints[len(paints)-1]:
                        print("Paint Not Found")
            case 3:
                print("\nEnter the details of the paint you would like to delete:")
                brand, color, sku = input("Brand: "), input("Color: "), input("SKU (0 for none): ")
                for paint in paints:
                    if paint == Paint(brand, color, sku):
                        print("\nPaint Deleted!")
                        paints.remove(paint)
                        break
                    if paint == paints[len(paints)-1]:
                        print("Paint Not Found")
            case 4:
                for i in range(0, len(paints)):
                    print(f"{i+1}: {sorted(paints)[i]}")
            case 5:
                display_main_menu()
                return 0
            case _:
                print("\nWARNING: Must be a number 1-5.\n")

def main():
    load_objects()
    display_main_menu()

main()