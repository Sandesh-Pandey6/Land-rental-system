from datetime import datetime, date
from time import localtime, strftime
from random import randint
from read import formatData, getLandsData, showBill

fileName = "land_info.txt"


def rentingBill(data):
    """
    Function to generate and print a renting invoice.
    It will take a list containing customer name, phone number, rented land IDs, and corresponding durations.
    """
    
    # Extract data from the input list
    name = data[0]
    phone = data[1]
    rentingList = data[2]
    rentingDuration = data[3]

    # Get the current date
    current_date = str(date.today())

    # Get the current time
    current_time = strftime("%I:%M:%S", localtime())
    
    # Generate a random invoice ID
    invoiceID = str(randint(100000, 900000))

    # Construct the invoice name
    invoiceName = "Invoices"+"/"+"Renting-Invoice-" + invoiceID + ".txt"

    # Open the invoice file
    file = open(invoiceName, "w")

    # Write invoice header and customer details
    file.write(
        "----------------------------------------- Invoice ------------------------------------------------"
    )

    file.write("\n\n\n")

    file.write(
        "    " + formatData("Invoice ID: " + invoiceID, 70) + "Date: " + current_date
    )

    file.write(
        "\n\n    " + formatData("Customer Name: " + name, 70) + "Time: " + current_time
    )

    file.write("\n\n    " + formatData("Customer Phone: " + str(phone), 70))

    file.write(
        "\n\n   ----------------------------------------------------------------------------------------------   \n\n"
    )

    file.write(
        "    SN  Kitta number  Location      Direction  Anna    Rent        Duration     Total     \n\n"
    )

    # Get lands data
    landsDataDict = getLandsData()

    grandTotal = 0

    # Write rented land details to the invoice
    for i in range(len(rentingList)):

        SN = str(i + 1)
        kittaNumber = str(rentingList[i])
        duration = str(rentingDuration[i])
        location = landsDataDict[str(rentingList[i])][0]
        direction = landsDataDict[str(rentingList[i])][1]
        anna = landsDataDict[str(rentingList[i])][2]
        rent = landsDataDict[str(rentingList[i])][3]

        file.write("    " + formatData(SN, 3))
        file.write(" " + formatData(kittaNumber, 13))
        file.write(" " + formatData(location, 13))
        file.write(" " + formatData(direction, 10))
        file.write(" " + formatData(anna, 7))
        file.write(" " + formatData(rent, 11))
        file.write(" " + formatData(duration, 12))

        total = int(rentingDuration[i]) * int(rent)

        file.write(" " + formatData(str(total), 10))

        file.write("\n")

        grandTotal = grandTotal + total

    # Write grand total to the invoice
    file.write(
        "\n   ----------------------------------------------------------------------------------------------   \n"
    )

    file.write(
        "\n                                                                    Grand Total: "
        + str(grandTotal)
        + "\n\n"
    )

    # Display the invoice
    file.close()

    showBill(invoiceName)




def returningBill(landsID):
    """
    Function to generate and print a returning invoice.

    it will take the ID of the land being returned.
    """

    d = getLandsData()

    # Get the current date
    current_date = str(datetime.now().date())

    # Get the current time
    current_time = strftime("%I:%M:%S", localtime())

    # Generate a random invoice ID
    invoiceID = str(randint(100000, 900000))

    # Get customer name from land data
    # print(landsID,landsID[0])
    # print(landsID[0][5])
    name = d[landsID[0]][5]

    # Constructing the invoice name
    invoiceName =  "Invoices"+"/"+"Returning-Bill-" + invoiceID + ".txt"

    # Opening the invoice file
    file = open(invoiceName, "w")

    # Write invoice header and customer details
    file.write(
        "----------------------------------------------------- Invoice ----------------------------------------------------"
    )

    file.write("\n\n\n")

    file.write(
        "    " + formatData("Invoice ID: " + invoiceID, 88) + "Date: " + current_date
    )

    file.write(
        "\n\n    " + formatData("Customer Name: " + name, 88) + "Time: " + current_time
    )

    file.write(
        "\n\n    --------------------------------------------------------------------------------------------------------------   \n\n"
    )

    file.write(
        "    Kitta number  Location      Direction  Anna    Rent        Duration     Extra Duration  Fine      Total       \n\n"
    )
    
    allTotal = 0
    
    for each in landsID:

        kittaNumber = str(each)
        location = str(d[each][0])
        direction = str(d[each][1])
        anna = str(d[each][2])
        rent = int(d[each][3])
        duration = int(d[each][6])

        total = duration * rent

        # calculating extra dureation for fine

        rentedDate = datetime.strptime(d[landsID[0]][7], "%Y-%m-%d")
        current_date = datetime.now()
        date_difference = current_date - rentedDate

        usedMonths = int(date_difference.days / 30)

        extraMonths = usedMonths - duration
    

        if extraMonths < 0:

            extraMonths = 0
        

        fineAmount = (rent * extraMonths) + (10 / 100 * (rent * extraMonths))

        total = total + fineAmount

        file.write("    " + formatData(kittaNumber, 13))
        file.write(" " + formatData(location, 13))
        file.write(" " + formatData(direction, 10))
        file.write(" " + formatData(anna, 7))
        file.write(" " + formatData(str(rent), 11))
        file.write(" " + formatData(str(duration), 12))
        file.write(" " + formatData(str(extraMonths), 15))
        file.write(" " + formatData(str(fineAmount), 9))
        file.write(" " + formatData(str(total), 16) + "\n")
        
        allTotal = allTotal + total
        
        changeStatus(each, "None", 0, "Available")


    file.write("\n")

    file.write(
        "\n    ---------------------------------------------------------------------------------------------------------------   \n"
    )

    file.write(
        "\n                                                                                         Grand Total: "
        + str(allTotal)
        + "\n\n"
    )
    
    file.close()

    showBill(invoiceName)


def writeNewData(d):

    file = open(fileName, "w")

    for id, val in d.items():

        file.write("  " + str(id) + "  ")

        for each in val:

            file.write(",  " + str(each) + "  ")

        file.write("\n")

    file.close()


def changeStatus(id, cust, month, status):
    """
    Function to change the status of a land (Available/Not Available) and update customer details and renting duration.

    It will take :
        1) id (str): The ID of the land.
        2) cust (str): The name of the customer.
        3) month (int): The renting duration in months.
        4) status (str): The status of the land (Available/Not Available).
    """


    # Get lands data
    d = getLandsData()

    # Update land status, customer details, and renting duration
    d[id][4] = status

    d[id][5] = cust

    d[id][6] = month

    # Update renting date based on status
    if status == "Available":

        d[id][7] = "Renting Date Here"

    elif status == "Not Available":

        d[id][7] = str(datetime.now().date())

    # Write updated data to the file
    writeNewData(d)
