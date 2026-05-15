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
                words = [word.strip() for word in line.split(",", 3)]
                projects.append(Project(words[0], words[1], words[2], json.loads(words[3])))       
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
                if not projects:
                    print("No projects added yet.")
                    continue

                print("Please enter the number of the project you wish to open (0 to load more): ")
                project_choice = get_input_from_list(projects, "Project")
                display_projects_menu(projects[project_choice-1])
                return 0
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
                        file.write(f"{mini.game}, {mini.faction}, {mini.name}\n")

                with open(paint_csv, "w") as file:
                    for paint in paints:
                        file.write(f"{paint.brand}, {paint.color}, {paint.sku}\n")

                with open(project_csv, "w") as file:
                    for project in projects:
                        file.write(f"{project.category}, {project.name}, {project.description}, {json.dumps(project.minis)}\n")
                        

                return 0 
            case _:
                print("\nWARNING: Must be a number 1-6.")

def display_projects_menu(project):
    while True:
        try:
            choice = int(input("\n1. Add a Mini\n2. View Minis\n3. Paint a Mini\n4. Change Mini Status\n5. Change Mini Amount\n6. Edit/Delete Project\n7. Exit\n"))
        except ValueError:
            print("\nWARNING: Must be a number 1-7.\n")
            continue

        match choice:
            case 1:
                if not miniatures:
                    print("No miniatures available.")
                    continue

                print("Please enter the number of the mini you wish to add (0 to load more): ")
                mini_choice = get_input_from_list(miniatures, "Mini")
                project.add_mini(miniatures[mini_choice-1], 1)
            case 2:
                project.print_minis()
            case 3:
                if not project.minis:
                    print("No minis added to project yet.")
                    continue

                print("Please enter the number of the mini you wish to paint (0 to load more): ")
                mini_choice = get_input_from_list(project.minis, "Mini", 1)
                
                if not paints:
                    print("No paints available.")
                    continue
                    
                print("Please enter the number of the paint you'd like to apply (0 to load more): ")
                paint_choice = get_input_from_list(paints, "Paint")
                if f"{str(paints[paint_choice-1])} " in project.minis[str(mini_choice)]["Paints"]:
                    print("Paint already added!")
                    continue
                project.minis[str(mini_choice)]["Paints"] += f"{str(paints[paint_choice-1])} "
            case 4:
                if not project.minis:
                    print("No minis added to project yet.")
                    continue

                print("Please enter the number of the mini you wish to paint (0 to load more): ")
                mini_choice = get_input_from_list(project.minis, "Mini", 1)
                
                status_choice = 0
                status_key = ""
                while status_choice == 0:
                    try:
                        status_choice = int(input("Which status do you want to change it to?\n1. On-Sprue\n2. Assembled\n3. Primed\n4. Painted\n"))
                    except ValueError:
                        print("Please enter a number 1-4.")
                    
                    match status_choice:
                        case 1:
                            status_key = "On-Sprue"
                        case 2:
                            status_key = "Assembled" 
                        case 3:
                            status_key = "Primed"
                        case 4:
                            status_key = "Painted"
                        case _:
                            print("Please enter a number 1-4.")

                amount_choice = 0
                while amount_choice == 0:
                    try:
                        amount_choice = int(input("How many do you want to change?\nAmount: "))
                    except ValueError:
                        print("Not a number! Please try again.")
                    if amount_choice > project.minis[str(mini_choice)]["Amount"]:
                        print(f"There's only {project.minis[str(mini_choice)]["Amount"]} available!")
                        amount_choice = 0

                project.change_mini_status(str(mini_choice), status_key, amount_choice) 
            case 5:
                if not project.minis:
                    print("No minis added to project yet.")
                    continue

                print("Please enter the number of the mini you wish to change (0 to load more): ")
                mini_choice = get_input_from_list(project.minis, "Mini", 1)

                amount_choice = -1
                while amount_choice == -1:
                    try:
                        amount_choice = int(input("What is the amount of this mini?\nAmount: "))
                    except ValueError:
                        print("Not a number! Please try again.")
                
                project.change_mini_amount(str(mini_choice), amount_choice)
            case 6:
                project_edit_choice = 0
                while project_edit_choice == 0:
                    try:
                        project_edit_choice = int(input("Which part of the project do you want to edit?\n1. Category\n2. Name\n3. Description\n4. Delete Project\n"))
                    except ValueError:
                        print("Please enter a number 1-4.")
                    
                    match project_edit_choice:
                        case 1:
                            project_category = input("What would you like to change the category to?\nCategory: ")
                            project.category = project_category
                        case 2:
                            project_name = input("What would you like to change the name to?\nName: ")
                            project.name = project_name
                        case 3:
                            project_description = input("What would you like to change the description to?\nDescription: ")
                            project.description = project_description
                        case 4:
                            if input("Are you sure you want to delete the project? (y/n)\n ").lower() == "y":
                                projects.remove(project)
                                del project
                                print("Project deleted.")
                                display_main_menu()
                                return 0
                            else:
                                print("Deletion Aborted")
                        case _:
                            print("Please enter a number 1-4.")
            case 7:
                display_main_menu()
                return 0
            case _:
                print("\nWARNING: Must be a number 1-7.\n") 

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

def get_input_from_list(list, subject, dict=0):
    user_choice = 0
    list_start = 0
    list_end = 5
    while user_choice == 0:
        for i in range(list_start, list_end):
            try:
                if dict == 1:
                    print(f"{i+1}. {list[str(i+1)]["Mini"]}")
                elif dict == 0:
                    print(f"{i+1}. {list[i]}")
            except (IndexError, KeyError):
                continue
        list_start += 5
        list_end += 5
        try:
            user_choice = int(input(f"{subject} Number: "))
        except ValueError:
            print("Not a number! Please try again.")
            continue
        if user_choice < 1 or user_choice > len(list):
            print("Invalid Number! Please choose again.")
            user_choice = 0
        if list_start > len(list) and user_choice == 0:
            print(f"All {subject}s printed, looping back to start.")
            list_start = 0
            list_end = 5
    return user_choice

def main():
    load_objects()
    display_main_menu()

main()