
# Importing necessary modules
from operation import rent, returnLand
from write import rentingBill, returningBill, changeStatus
from read import displayLandInfo

'''
This serves as the entry point for the Land Rental System. It displays the welcome message,
prompts the user to select an option (Rent, Return, or Exit), and then executes the corresponding action.
'''


print(
    "\n\n------------------------- WELCOME TO TECHNO PROPERTY NEPAL -------------------------\n"
)

displayLandInfo() # Displaying information about lands

# Prompt user to select an option
print("\nPlease select any option: ")
print("\n1. Rent")
print("\n2. Return")
print("\n3. Exit")

# Continue prompting user until a valid option is selected
while True:

    choice = input("\nWhat's your choice: ").lower()

    if choice == "1" or choice == "rent": 
        # Rent land
        data = rent()

        rentingBill(data)

    elif choice == "2" or choice == "return":
        # Return land
        
        returnLand()

        

    elif choice == "3" or choice == "exit":
        # Exit the program
        print("\nThank you for using our Service.")

        exit()

    else:
        # Invalid option
        print("\nChoose a valid option.")

        continue
    
    
    # Ask if the user wants to continue using the system
    while True:

        choice = input(
            "\nDo you want to continue running our land rental system ? (y/n): "
        ).lower()

        if choice == "y" or choice == "yes":

            break

        elif choice == "n" or choice == "no":
            
            print("\n################################ Thank you for using using our service. ################################\n")

            exit()

        else:
            # Invalid answer
            print("\nChoose a valid answer.")

            continue
