
# Importing necessary modules
from read import getLandsData
from write import changeStatus, returningBill
from read import formatData


def rent():
    """
    Function to handle the process of renting land.
    It returns a list containing customer name, phone number, list of rented land IDs, and corresponding durations.
    """
    
    # Get customer name
    while True:

        name = input("\nEnter customer name: ").title()

        if len(name) < 3:

            print("\nPlease enter a valid name")

        else:

            break

    # Get customer phone number
    while True:
        
        try:
            
            phone = formatData(input("\nEnter customer phone: "))

            if len(phone) < 10 and int(phone) < 9000000000:

                print("\nEnter a valid phone number")

            else:

                break
            
        except:
            
            print("Please enter a valid phone number")
      
    # Get lands data
    landsDataDict = getLandsData()

    # renting = True


    # Initializing lists to store rented land IDs and durations
    rentingList = []

    rentingDuration = []

    # Loop to select lands for rent
    while True:

        try:
            # Get land ID
            landID = input("\nEnter kitta no. of the land: ")

            if landID not in landsDataDict:

                print("\nEnter a valid land id.")

                continue

            elif landID in rentingList:

                print(
                    "\nThis land is already added to your invoice. Please select another one."
                )

                continue

            elif formatData(landsDataDict[landID][4]) == "Not Available":

                print("\nThis land is already rented. Please select another one.")

                continue

            else:

                rentingList.append(landID)

        except:

            print("\nEnter a valid land id.")

        # Get renting duration
        while True:

            try:

                duration = int(input("\nFor how many months he/she wants to rent ? : "))

                if duration < 1 or duration > 360:

                    print("\nEnter months between 1 and 360 months.")

                    continue

                else:

                    rentingDuration.append(duration)

                    break

            except:

                print("\nEnter valid number of months.")

        # Asking if more land is to be rented
        choice = input("\nDo he/she wants to rent more land(y/n): ")

        if choice == "yes" or choice == "y":

            continue

        else:

            break
        
    # Updating status of rented lands
    for i in range(len(rentingList)):

        changeStatus(rentingList[i], name, rentingDuration[i], "Not Available")

    return [name, phone, rentingList, rentingDuration]




def returnLand():
    """
    Function to handle the process of returning rented land.
    It returns the ID of the land to be returned.
    """

    # Get lands data
    d = getLandsData()
    
    returningLands = []

    # Loop to select land to return
    while True:
    

        landID = input("\nEnter kitta number of the land to return : ")
        
        try:
            
            if formatData(d[landID][4].lower()) == "available":
            
                print("\nThis land has not been rented yet. Please select another land. ")
            
                continue
            
        except:
            
            print("\nPlease choose a valid kitta number.")
            
            continue 
            
            
        
        if landID not in d:
            
            print("\nThis land is not in the list. Please choose a valid kitta number.")
            
            continue         
            
        sameUser = False

        for each in returningLands:
            
            name = formatData(d[each][5].lower())
            custName = formatData(d[landID][5].lower())
            
            if custName != name:
                
                print("\nThis customer has not rented this land.")
                
                sameUser = True
                
        ask = True
                
        if sameUser == True:
            
            sameUser = False
            
            choice = input("\nDo you want to return more land ? (y/n): ")
            
            if choice == "yes" or choice == "y":
            
                continue
            
            else:
                
                ask = False
             
        elif landID in returningLands:
            
            print("\nThis land is already added to the bill. Please select another land.")
            
            continue            

        else:

            returningLands.append(landID)

        if ask == True:
            
            choice = input("\nDo you want to return more land(y/n): ").lower()
            
            if choice == "yes" or choice == "y":
                
                continue
            
            else:
                
                break
            
        else:
            
            break

    returningBill(returningLands)


# returnLand()
