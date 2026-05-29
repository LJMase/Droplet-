import os
import json
from mini import Mini 
from project import Project 
from paint import Paint 

# Initializing filepaths and lists to store all miniatures, paints, and projects
mini_csv, paint_csv, project_csv = "./miniatures.csv", "./paints.csv", "./projects.csv"
miniatures = []
paints = []
projects = []

def load_objects():
    # This helper function loads all the csv files from the filepath variables and turns their data into the actual objects.
    # This is used to keep data saved between program uses. Each section starts by checking if there's a file at a given filepath and if not, creates a new csv.
    # If the file exists, we open it in read mode and seperate each word in each line to create objects with them. 
    # For mini, this is taking the game, faction, and name, and then creating a Mini object with those variables. This recreates all previous data stored in the csv. 

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

    # The project_csv handles things a little differently as projects utilize nested dictionaries, which are hard to store in a csv file. 
    # To handle this, JSON is used to write and load the nested dictionaries from the file. 
    if os.path.isfile(project_csv):  
        with open(project_csv, "r") as file:
            for line in file:
                words = [word.strip() for word in line.split(",", 3)]
                projects.append(Project(words[0], words[1], words[2], json.loads(words[3])))       
    else:
        print("No project file found. Creating new file...")
        with open(project_csv, "w"):
            pass 

def display_main_menu() -> int:
    # This display helper function prints the interactable main menu for the program. I use a while True loop and match-case to ensure to get valid user input and perform the appropriate action. 
    # There are 6 options for the main menu: Open a project, create a project, view all projects, change miniatures, change paints, and exit. 

    while True:
        # This try except block ensures a given input is an integer
        try:
            choice = int(input("\nWelcome to Droplet! What would you like to do?\n1. Open a Project\n2. Create a Project\n3. View All Projects\n4. Change Miniatures\n5. Change Paints\n6. Exit\n"))
        except ValueError:
            print("\nWARNING: Must be a number 1-6.")
            continue
            
        match choice:
            # Case 1 makes sure a project has been created, and then uses get_input_from_list() to display all projects in the projects list and get user input for which project to open.
            # Then, the projects menu is opened with display_projects_menu(), passing in the chosen project from the projects list. 
            # Return 0 is used to exit this while loop before entering the while loop of display_projects_menu()
            case 1:
                if not projects:
                    print("\nNo projects added yet.")
                    continue

                print("\nPlease enter the number of the project you wish to open (0 to load more): ")
                project_choice = get_input_from_list(projects, "Project")
                display_projects_menu(projects[project_choice-1])
                return 0

            # Case 2 gets 3 string values from the user with no restrictions and creates a project using those 3 values, appending it to the projects list. 
            case 2:
                print("\nEnter the project category, name, and description.")
                project_category, project_name, project_description = input("Category: "), input("Name: "), input("Description: ")
                projects.append(Project(project_category, project_name, project_description))

            # Case 3 uses a for loop to print every project in the projects list. 
            case 3:
                print("--------Projects--------")
                for i in range(0, len(projects)):
                    print(f"{i+1}. {sorted(projects)[i]}")

            # Case 4 displays the miniatures menu using display_miniatures_menu() and then returning 0 to end this function's while loop.
            case 4:
                display_miniatures_menu()
                return 0

            # Case 5 displays the paints menu using display_paints_menu() and then returning 0 to end this function's while loop.
            case 5:
                display_paints_menu()
                return 0

            # Case 6 exits the program with return 0, however the current data and changes must be exported to the csv files in order to save the data across uses. 
            # Each file from the filepaths is opened in write mode, and then we loop through all the objects in each list (projects, minis, and paints) writing each object and it's attributes to a line in the csv.  
            case 6:
                with open(mini_csv, "w") as file:
                    for mini in miniatures:
                        file.write(f"{mini.game}, {mini.faction}, {mini.name}\n")

                with open(paint_csv, "w") as file:
                    for paint in paints:
                        file.write(f"{paint.brand}, {paint.color}, {paint.sku}\n")

                # As mentioned earlier in the loading portion, projects is a special case due to it's use of nested dictionaries. JSON is used to write the nested dictionaries to the csv. 
                with open(project_csv, "w") as file:
                    for project in projects:
                        file.write(f"{project.category}, {project.name}, {project.description}, {json.dumps(project.minis)}\n")
                return 0 
            
            # This wildcard case catches all input that is a valid integer but outside of the 1-6 range. 
            case _:
                print("\nWARNING: Must be a number 1-6.")

def display_projects_menu(project: Project):
    # Similar to display_main_menu(), this display helper function prints the interactable menu for everything project related. I use a while True loop and match-case to ensure to get valid user input and perform the appropriate action. 
    # There are 7 options for the projects menu: Adding a mini to the project, Viewing the minis in the project, Adding paint to a mini, Changing the status of minis, 
    # Changing the amount of minis, Editing the project attributes or deleting it, and going back to the main menu. 

    while True:
        try:
            choice = int(input("\n1. Add a Mini\n2. View Minis\n3. Paint a Mini\n4. Change Mini Status\n5. Change Mini Amount\n6. Edit/Delete Project\n7. Exit\n"))
        except ValueError:
            print("\nWARNING: Must be a number 1-7.")
            continue

        match choice:
            case 1:
                if not miniatures:
                    print("\nNo miniatures available.")
                    continue

                print("\nPlease enter the number of the mini you wish to add (0 to load more): ")
                mini_choice = get_input_from_list(miniatures, "Mini")
                project.add_mini(miniatures[mini_choice-1], 1)
            case 2:
                project.print_minis()
            case 3:
                if not project.minis:
                    print("\nNo minis added to project yet.")
                    continue

                print("\nPlease enter the number of the mini you wish to paint (0 to load more): ")
                mini_choice = get_input_from_list(project.minis, "Mini", 1)
                
                if not paints:
                    print("\nNo paints available.")
                    continue
                    
                print("\nPlease enter the number of the paint you'd like to apply (0 to load more): ")
                paint_choice = get_input_from_list(paints, "Paint")
                if f"{str(paints[paint_choice-1])} " in project.minis[str(mini_choice)]["Paints"]:
                    print("Paint already added!")
                    continue
                project.minis[str(mini_choice)]["Paints"] += f"{str(paints[paint_choice-1])} "
            case 4:
                if not project.minis:
                    print("\nNo minis added to project yet.")
                    continue

                print("\nPlease enter the number of the mini you wish to paint (0 to load more): ")
                mini_choice = get_input_from_list(project.minis, "Mini", 1)
                
                status_choice = 0
                status_key = ""
                while status_choice == 0:
                    try:
                        status_choice = int(input("\nWhich status do you want to change it to?\n1. On-Sprue\n2. Assembled\n3. Primed\n4. Painted\n"))
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
                print("\nWARNING: Must be a number 1-7.") 

def display_miniatures_menu() -> int:
    # Similar to display_main_menu(), this display helper function prints the interactable menu for everything miniature related. I use a while True loop and match-case to ensure to get valid user input and perform the appropriate action. 
    # There are 5 options for the minis menu: Adding a mini, Editing a mini, Deleting a mini, Viewing miniatures, and going back to the main menu. 

    while True:
        # This try except block ensures a given input is an integer
        try:
            choice = int(input("\nWhat would you like to do?\n1. Add a Mini\n2. Edit a Mini\n3. Delete a Mini\n4. View Miniatures\n5. Go Back\n"))
        except ValueError:
            print("\nWARNING: Must be a number 1-5.")
            continue
        
        match choice:
            # Case 1 gets 3 strings from user input with no restrictions and creates a Mini object with them. 
            case 1:
                print("\nPlease enter the game(40k, D&D, etc.), the faction, and the name of the miniature.")
                miniatures.append(Mini(input("Game: "), input("Faction: "), input("Name: "))) 

            # Case 2 gets 3 strings from user input and loops through the miniatures list to find a matching mini object. The user then inputs the 3 new attributes for said mini, it is changed, and the option is exited. 
            case 2:
                print("\nEnter the details of the miniature you would like to edit: ")
                game, faction, name = input("Game: "), input("Faction: "), input("Name: ")

                for mini in miniatures: 
                    if mini == Mini(game, faction, name):
                        print("\nMini Found! Enter the new details below:")
                        new_game, new_faction, new_name = input("New Game: "), input("New Faction: "), input("New Name: ")
                        mini.game, mini.faction, mini.name = new_game, new_faction, new_name
                        break # Break is used to avoid the for loop continuing after a successful edit and eventually printing mini not found.

                    # Mini not found should only be printed after the entire list has been checked, so I check if we're on the last element before printing mini not found. 
                    if mini == miniatures[len(miniatures)-1]:
                        print("Mini Not Found")

            # Case 3 gets 3 strings from user input and loops through the paints list to find a matching paint object, which gets deleted. 
            case 3:
                print("\nEnter the details of the miniature you would like to delete:")
                game, faction, name = input("Game: "), input("Faction: "), input("Name: ")

                for mini in miniatures:
                    if mini == Mini(game, faction, name):
                        print("\nMini Deleted!")
                        miniatures.remove(mini)
                        break # Break is used to avoid the for loop continuing after a successful edit and eventually printing mini not found.

                    # Mini not found should only be printed after the entire list has been checked, so I check if we're on the last element before printing mini not found. 
                    if mini == miniatures[len(miniatures)-1]:
                        print("Mini Not Found")

            # Case 4 loops through the miniatures list and prints each object.
            case 4:
                print("--------Miniatures--------")
                for i in range(0, len(miniatures)):
                    print(f"{i+1}: {sorted(miniatures)[i]}")
                
            # Case 5 calls display_main_menu() to start it's while loop and display options, and then returns 0 to exit this menu. 
            case 5:
                display_main_menu()
                return 0

            # This wildcard case catches all input that is a valid integer but outside of the 1-5 range. 
            case _:
                print("\nWARNING: Must be a number 1-5.")

def display_paints_menu() -> int:
    # Similar to display_main_menu(), this display helper function prints the interactable menu for everything paint related. I use a while True loop and match-case to ensure to get valid user input and perform the appropriate action. 
    # There are 5 options for the paints menu: Adding a paint, Editing a paint, Deleting a paint, Viewing paints, and going back to the main menu. 

    while True:
        # This try except block ensures a given input is an integer
        try:
            choice = int(input("\nWhat would you like to do?\n1. Add a Paint\n2. Edit a Paint\n3. Delete a Paint\n4. View Paints\n5. Go Back\n"))
        except ValueError:
            print("\nWARNING: Must be a number 1-5.")
            continue

        match choice:
            # Case 1 gets 3 strings from user input with no restrictions and creates a Paint object with them. 
            case 1:
                print("\nPlease enter the name, the brand, and the SKU (if N/A, enter 0).")
                paints.append(Paint(input("Brand: "), input("Color: "), input("SKU: "))) 

            # Case 2 gets 3 strings from user input and loops through the paints list to find a matching paint object. The user then inputs the 3 new attributes for said paint, it is changed, and the option is exited. 
            case 2:
                print("\nEnter the details of the paint you would like to edit: ")
                brand, color, sku = input("Brand: "), input("Color: "), input("SKU (0 for none): ")

                for paint in paints: 
                    if paint == Paint(brand, color, sku):
                        print("\nPaint Found! Enter the new details below:")
                        new_brand, new_color, new_sku = input("New Brand: "), input("New Color: "), input("New SKU: ")
                        paint.brand, paint.color, paint.sku = new_brand, new_color, new_sku
                        break # Break is used to avoid the for loop continuing after a successful edit and eventually printing paint not found.

                    # Paint not found should only be printed after the entire list has been checked, so I check if we're on the last element before printing paint not found. 
                    if paint == paints[len(paints)-1]:
                        print("Paint Not Found")
            
            # Case 3 gets 3 strings from user input and loops through the paints list to find a matching paint object, which gets deleted. 
            case 3:
                print("\nEnter the details of the paint you would like to delete:")
                brand, color, sku = input("Brand: "), input("Color: "), input("SKU (0 for none): ")

                for paint in paints:
                    if paint == Paint(brand, color, sku):
                        print("\nPaint Deleted!")
                        paints.remove(paint)
                        break # Break is used to avoid the for loop continuing after a successful edit and eventually printing paint not found.

                    # Paint not found should only be printed after the entire list has been checked, so I check if we're on the last element before printing paint not found. 
                    if paint == paints[len(paints)-1]:
                        print("Paint Not Found")

            # Case 4 loops through the paints list and prints each object.
            case 4:
                print("--------Paints--------")
                for i in range(0, len(paints)):
                    print(f"{i+1}: {sorted(paints)[i]}")

            # Case 5 calls display_main_menu() to start it's while loop and display options, and then returns 0 to exit this menu. 
            case 5:
                display_main_menu()
                return 0

            # This wildcard case catches all input that is a valid integer but outside of the 1-5 range. 
            case _:
                print("\nWARNING: Must be a number 1-5.")

def get_input_from_list(list: list | dict, subject: str, dict=0) -> int:
    # get_input_from_list() is a helper function designed to print out all the objects in a list (or dict) and have the user select one. 
    # It takes in a list/dict to iterate through and a subject to know what to display to the user. The dict variable is used to tell the function whether a dictionary or list is being used. 
    # I use this function primarily for lists, but do need to print the miniatures inside of a project dictionary, which is why the dict variable and dict functionality exist.  
    # Because having a user select an item from a list through retyping it's exact attributes is inconvenient at best (and my program requires that a lot), I created this method. 

    user_choice = 0
    list_start = 0 # List start and list end determine how many objects to display at once. By default 5 objects are displayed per page. 
    list_end = 5

    # A while loop is used to ensure valid user input is given. 0 is used to loop again and print the next page of 5 objects. 
    while user_choice == 0: 
        for i in range(list_start, list_end): 
            # Because 5 objects are printed at a time, I use a try except to avoid any errors if the list does not have 5 objects left to print. 
            try:
                if dict == 1: # For the dictionary case I specifically print the values of the Mini sub dictionary in a project as this is it's only use in the program. 
                    print(f"{i+1}. {list[str(i+1)]["Mini"]}")
                elif dict == 0: # 0 is the default and the normal list case. This just prints the values of the list. 
                    print(f"{i+1}. {list[i]}")
            except (IndexError, KeyError):
                continue
        
        # Try except is used to get valid integer input from the user 
        try:
            user_choice = int(input(f"\n{subject} Number: ")) 
        except ValueError:
            print("Not a number! Please try again.")
            continue

        # Once valid integer input is obtained, this is used to make sure the user_choice will not cause an index_error. 
        if (user_choice < 0 or user_choice > len(list)):
            print("Invalid Number! Please choose again.")
            user_choice = 0
            continue
        
        # Increment the list_start and list_end variables to display the next 5 objects when the for loop runs again
        list_start += 5
        list_end += 5
        
        # If the new list_start is greater than the length of the list, I reset everything back to 0 and display the first 5 objects again. 
        # This way the user can loop through the objects as many times as necessary. 
        if list_start > len(list) and user_choice == 0:
            print(f"All {subject}s printed, looping back to start.")
            list_start = 0
            list_end = 5

    return user_choice

def main():
    # The use of main feels a little pointless to me due to only having 2 helper functions, but it calls my two helper functions, load_objects() to initialize everything and display_main_menu() to get the program started. 
    load_objects()
    display_main_menu()

main()