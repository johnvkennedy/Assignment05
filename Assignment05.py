# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Jack Kennedy,11/17/2020,Editing Script for Assignment):
# RRoot,1.1.2030,Created started script
# <Jack Kennedy>,<11/17/2020>,Added/Edited code to complete assignment 5
# ------------------------------------------------------------------------ #

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# Personal Notes to Translate Meaning to Self (Jack):
# The purpose of the script is for the user to input two pieces of information
# that will be into an *Dictionary*. There will be !!1 Dictionary, 1 ROW!!
# representing each data set. These will then be put into a SINGLE list to create
# the equivilant of a table of data. All this will be saved to a file named
# "mytodolist" where the data will be appended as to not delete previous data.
# Path to file is - "C:\_PythonClass\mytodolist.txt"

# Flow of work:
# Open "ToDo - Put input data into Dictionary - Put Dictionary into a List - Use list to print and save
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# -- Data -- #
# declare variables and constants
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
txtdata = []   # ADDED = Data for the text document


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# This took forever to figure out. Didn't realize for a while how to put a list into a dictionary.
# These lines take the data in the file, then format them into a dictionary split with the two data
# sets. The dictionary names are decided at the start then the list data is put in. Trying to explain
# it to myself because it was really confusing.
#       At the end "dicRow" is given a value to be used later on. This is to take data out of the
# text file to save as a variable.
objFile = open("C:\_PythonClass\mytodolist.txt")
for row in objFile:
    txtdata = row.split(",")
    dicRow = {"Task": txtdata[0], "Priority": txtdata[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
print("==============================================\n"
      "\t Hello amazing user!\n"
      "\t This script is made to allow you to\n"
      "\t view, add, and remove items of a\n"
      "\t list made in -mytodolist.txt-. There is\n"
      "\t also an option to save that data.\n\n"
      "\t First it will open the file to keep\n"
      "\t previously existing data then you the\n"
      "\t user may interact with that data.\n\n"
      "\t            !IMPORTANT!\n"
      "\t DATA IS ONLY SAVED WHEN THE OPTION\n"
      "\t       IS CHOSEN IN THE MENU!\n"
      "==============================================")

while (True):
    print("""
    *** Menu of Options ***
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks


    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # NOTE - Use "read" to display the data. Will need to use
        #        a small loop to make it go vertical, refer to previous
        #        assignment on the code needed. The data does not change
        #        here, it's only displayed then goes back to loop.

        print("--------------------------------------------\n"
              "\tThis is the current data in the table.\n"
              "--------------------------------------------\n"
              "==============")
        print("Row - Task - Priority")
        counter = 0
        for row in lstTable:
            print(f'{counter} | {row["Task"]} | {row["Priority"]} |')
            counter += 1
        print("==============")
        continue


    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newtask = input("-------------------------------------------------\n"
                        "\tYou've chosen to add to the current table.\n"
                        "\tWhat task do you wish to add?\n"
                        "-------------------------------------------------\n"
                        "\tEnter New Task: ")
        newpriority = input("\n---------------------------------------------------------------\n"
                            "\tWhat priority do you wish to designate to this task?\n"
                            "\tExamples: 1-10, Not Important to Important, Low to High.\n"
                            "---------------------------------------------------------------\n"
                            "\tEnter Priority for New Task: ")
        dicRow = {"Task":newtask, "Priority":newpriority}
        lstTable.append(dicRow)
        print("\n=====",newtask,"has been added with priority",newpriority,"=====")
        continue


    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # Previous lines before rereading the assignment. Works, just not to the extent needed.
        # del lstTable[-1]
        # print("--------------------------------------------------\n"
        #      "\t You've selected to remove\n"
        #      "\t The newest or last task and priority has\n"
        #      "\t been removed from the current table\n"
        #      "--------------------------------------------------\n")
        removal = int(input("--------------------------------------------------\n"
                            "\tThe option to remove a row has been chosen\n"
                            "\tWhich row do you wish to delete?\n"
                            "--------------------------------------------------\n"
                            "\tRow to Delete: "))
        lstTable.pop(removal) # NEEDS TO BE AN INTERGER!!
        print("\n===== Row",removal,"has been taken out of the table =====")

        continue


    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # NOTE - ALL DATA BEFORE THIS POINT IS NOT SAVED TO THE TEXT FILE!!!!!!
        # This is the point at which that's done. Open the file then write the
        # list inside. Before this point the data is saved in memory, NOT HARDWARE!!
        # NOTE TO SELF - Figured out the problem. The dictionary sections needed
        # to be in lists not strings.
        objFile = open("C:\_PythonClass\mytodolist.txt","w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        print("===== The current table has been saved =====\n")
        continue


    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("======================================\n"
              " Thank you for using the script.\n"
              " The script has ended. Please hit any\n"
              " key to close out of the script.\n"
              "======================================")
        break  # and Exit the program
