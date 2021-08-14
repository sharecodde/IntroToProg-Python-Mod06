##----------------------------------------------------------------------------  #
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
# BGilbertson, 8.13.2021,Added enter new task code, remove task
# BGilbertson, 8.14.2021,Put the code pieces together
# BGilbertson, 8.15.2021,More code testing, commenting, and finalizing

# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
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
        """ Adds task and priorities to list"""
        row = {"Task": task.strip(), "Priority": priority.strip()}
        list_of_rows.append(row)
        return list_of_rows, 'Success'

    # @staticmethod
    # def remove_data_from_list(task, list_of_rows):
    #     """ Removes task from list of dictionaries
    #     :param task: (string) task we want to remove:
    #     :param list_of_rows: (list) of dictionary rows
    #     :return: (list) of dictionary rows
    #     """
    #     task = task.strip() # task to be removed
    #     task = task.lower()
    #     list_of_rows_local = []   # local list to write the new rows to
    #     for row in list_of_rows:
    #         task_local = row["Task"]
    #         if task != task_local:   # remove the user selected task
    #             list_of_rows_local.append(row)
    #     list_of_rows.clear()  # clear contents
    #     list_of_rows = list_of_rows_local    # populate with current list
    #     return list_of_rows

    @staticmethod # NOT DONE
    def remove_data_from_list(task, list_of_rows):
        """--- removes task for the list---"""
        for row in list_of_rows:
            if row["Task"].lower() == task.lower():
                lstTable.remove(row)
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_from_list(file_name, list_of_rows):
        """--writes data to the file strFileName (ToDoFile.txt)----"""
        objFile = open(file_name, "w")
        for row in list_of_rows:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        return list_of_rows, 'Success'
        #print("\nYour data has been saved.")


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

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
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
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

    # @staticmethod
    # def input_new_task_and_priority():
    #     strTask = str(input("\nEnter a task to do: "))
    #     strPriority = str(input("Enter its priority 'l' for low, 'h' for high: "))
    #     if strPriority.lower() == "l" or strPriority.lower() == "h": #checks for a valid priority entry
    #         print("The task: " + strTask + ",  " + "has been added to the list and its priority is:  " + strPriority)
    #     else:
    #         print("Please enter only 'l' or 'h' for priority")
    #     # return task, priority

    @staticmethod
    def input_new_task_and_priority():
        task = str(input("\nEnter a task to do: ")) #Try here in IO section
        priority = str(input("Enter its priority 'l' for low, 'h' for high: ")) #Try here in IO section
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Asks user which task they would like to remove
        :return: (string) task
        """
        task = str(input("Enter a task to remove: "))
        return task

    @staticmethod
    def say_goodbye():
        print("Here is a summary of all the items in your ToDo list.")
        print("=" * 50)
        IO.print_current_Tasks_in_list(lstTable)
        print("=" * 50)
        print("\nThank you, presss 'enter' to end the program.")
        input()

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        strTask, strPriority = IO.input_new_task_and_priority()  # (strTask,strPriority)
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
            #IO.print_current_tasks_in_list(lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled")
        continue #shows the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable.clear() #clear the table
            Processor.read_data_from_file(strFileName, lstTable)
            IO.print_current_Tasks_in_list(lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu


    elif strChoice == '5':  # Exit Program
        IO.say_goodbye()
        print("Goodbye!")
        break  # and Exit
