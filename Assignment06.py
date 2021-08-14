#----------------------------------------------------------------------------  #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# BGilbertson, 8.11.2021,Added header
# BGilbertson, 8.12.2021,Added menu print, enter choice, read data and save data code
# BGilbertson, 8.13.2021,Added enter new task code
# BGilbertson, 8.14.2021,Added header remove task and but the code pieces together
# BGilbertson, 8.15.2021,More code testing, commenting, and finalizing
# ---------------------------------------------------------------------------- #
# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
strCopyOriginal = "ToDoFileCopy.txt" #Captures the original text file that is used for menu option "4"
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of a processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds task and priorities to list
        :param task: name of task
        :param priority: name of priority
        :param list_of_rows: (list) you want filled with file data
        :return list_of_rows: list of dictionary rows
        """
        row = {"Task": task.strip(), "Priority": priority.strip()}
        list_of_rows.append(row)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """--- removes task from the list
        :param task: name of task to remove
        :param list_of_rows: (list) you want filled with file data
        :return list_of_rows: list of dictionary rows---"""
        for row in list_of_rows:
            if row["Task"].lower() == task.lower():
                lstTable.remove(row)
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_from_list(file_name, list_of_rows):
        """--writes data to the file strFileName (ToDoFile.txt)----
        :param file_name: name of file
        :param list_of_rows: (list) you want filled with file data
        :return list_of_rows: list of dictionary rows
        """
        objFile = open(file_name, "w")
        for row in list_of_rows:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        return list_of_rows, 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_hello():
        '''introduces the program to the user'''
        print()
        print("~" * 90)
        print("""                   
                                WELCOME
            This program allows the user to manage items in a ToDo list 
            along with their priority. You may view, add, delete, save, ToDo
            items and their corresponding priority.\n""")
        print("~" * 90)

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("****** The current Tasks ToDo and their priority, (h) for high and (l) for low, are: ******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************************************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """Asks user what task and priority they would like to add
        :return: task and priority
        """
        task = str(input("\nEnter a task to do: "))
        priority = str(input("Enter its priority 'l' for low, 'h' for high: "))
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Asks user which task they would like to remove
        :return: (string) task
        """
        task = str(input("Please enter a task from you ToDo list to remove: "))
        return task

    @staticmethod
    def say_goodbye():
        """summarize the ToDo list items for the user and close the"""
        print("Here is a summary of all the items in your ToDo list.")
        print("=" * 90)
        IO.print_current_Tasks_in_list(lstTable)
        print("=" * 90)
        print("\nThank you, presss 'enter' to end the program.")
        input()

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data
Processor.write_data_from_list(strCopyOriginal, lstTable) #make a copy of the original data for option "4"
IO.print_hello() # display introductory message to the user

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu of choices
    strChoice = IO.input_menu_choice()  # Get menu option from user

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        strTask, strPriority = IO.input_new_task_and_priority()
        Processor.add_data_to_list(strTask, strPriority, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        strtask = IO.input_task_to_remove()
        Processor.remove_data_from_list(strtask, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_from_list(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled")
        continue #shows the menu

    elif strChoice == '4':  # Reload Data from File :
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from the original file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable.clear() #clear the table
            Processor.read_data_from_file(strCopyOriginal, lstTable) #reads a copy of the original data file
            IO.print_current_Tasks_in_list(lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu


    elif strChoice == '5':  # Exit Program
        IO.say_goodbye()
        print("Goodbye!")
        break  # and Exit
    else:  # This code catches incorrect menu choices by the user
        print("Please choose only 1, 2, 3, 4, or 5 from the menu\n")

