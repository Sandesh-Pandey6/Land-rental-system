# Defining the file path
filePath = "land_info.txt"


def formatData(string, length=0):
    """
    Function to format string data by removing leading and trailing spaces and adjusting its length.

    It will take :
        string (str): The string data to be formatted.
        length (int, optional): The desired length of the formatted string. Defaults to 0.

    It returns the formatted string.
    """
    
    # Remove leading and trailing spaces
    if len(string) < 2:

        string = string

    else:

        while string[0] == " ":

            string = string[1:]

        while string[-1] == " ":

            string = string[:-1]


    # Adjust string length
    if length == 0:

        return string

    elif length > len(string):

        while length != len(string):

            string += " "

        return string

    elif length < len(string):

        return string[0:length]

    return string


def displayLandInfo():
    """
    Function to display information about all lands in a formatted table.
    """

    # Open the file
    file = open(filePath, "r")

    # Read lines from the file
    lines = file.readlines()

    # Print table header
    print(
        "\n----------------------------------- All Lands -------------------------------------"
    )

    print("\n\tKitta  Location           Direction  Area    Rent         Status\n")

    # Iterating through each line
    for i in range(len(lines)):

        # Removing newline characters and split line into list
        lines[i].replace("\n", "")

        lines[i] = lines[i].split(",")

        # Print formatted data for each land
        print("\t", end="")

        print(formatData(str(lines[i][0]), 6), end="")
        print(" " + formatData(str(lines[i][1]), 18), end="")
        print(" " + formatData(str(lines[i][2]), 10), end="")
        print(" " + formatData(str(lines[i][3]), 7), end="")
        print(" " + formatData(str(lines[i][4]), 12), end="")
        print(" " + formatData(str(lines[i][5]), 15), end="")

        print()
    # Print table footer
    print(
        "\n-----------------------------------------------------------------------------------"
    )


def getLandsData():
    """
    Function to read land data from the file and return it as a dictionary.
    It will return dictionary containing land information.
    """
    
    # Initialize dictionary to store land data
    landsDataDict = {}

    # Open the file
    file = open(filePath, "r")

    # Read lines from the file
    lines = file.readlines()

    # Parse each line and add data to dictionary
    for line in lines:

        line = line.replace("\n", " ")

        line = line.split(",")

        key = formatData(line[0])

        val = []

        for i in range(1, len(line)):

            val.append(formatData(line[i]))

        landsDataDict[key] = val

    return landsDataDict


def showBill(invoiceName):
    """
    Function to display the contents of a billing invoice.

    It will take the name of the invoice file.
    """
    
    # Open the invoice file
    file = open(invoiceName, "r")

    # Read all lines from the invoice
    allLands = file.readlines()

    print("\n")
    # Print each line of the invoice
    for each in allLands:

        if "-- Invoice --" in each:

            print("   ", each, end="    ")

        else:

            print(each, end="    ")
            
    print()
