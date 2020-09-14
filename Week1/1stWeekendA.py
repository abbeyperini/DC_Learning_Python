# global so you don't lose everything if you exit function
tasks = []

# number validation
def is_number(input_num):
    try:
        input_num = int(input_num)
        return True
    except ValueError:
        print("Whoops! That is not a valid number.")

# main function
def todo():
    # menu
    print("""
        Press 1 to Add Task. 
        Press 2 to Delete Task.
        Press 3 to View All Tasks. 
        Press Q to Quit. 
    """)
    user_input = input("> ")

    # not validating menu input numbers because I'm only taking those exact inputs
    if user_input == "1":
        # add task
        # valid priority options
        priorities = ["high", "High", "high.", "High.", "low", "Low", "low.", "Low.", "medium", "Medium", "medium.", "Medium."]
        
        title = input("Name your task: ")
        priority = input("Is this task high, medium, or low priority? ")
        
        # input validation for priorities
        if priority in priorities:
            # add note to global tasks array
            tasks.append({"title": title, "priority": priority})
            todo()

        #kick back to menu if not a valid priority
        else:
            print("Invalid priority")
            todo()
        
    elif user_input == "2":
        # delete task

        # print all the tasks with index number
        for i in range(0, len(tasks)):
            print(f'{tasks[i]["title"]} - {str(i)}')
        # user enters index number to delete
        index_input = input("""
            Enter index number to delete a task or M to go back to the menu. 
            > 
        """)

        # allowing an option to not delete
        if index_input == "m" or index_input == "M":
            todo()

        # input validation for numbers
        elif is_number(index_input):
            index = int(index_input)
            # delete task if valid number is a valid index
            if index <= (len(tasks) - 1) and index >= 0:
                del tasks[index]
                todo()
            # kick back to menu if not a valid index number
            else:
                print("That is not a valid index number.")
                todo()
        # kick back to menu if not a valid integer
        else:
            print("That is not a valid number.")
            todo()

    elif user_input == "3":
        # view all tasks in format index - title - priority
        for i in range(0, len(tasks)):
            print(f'{i} - {tasks[i]["title"]} - {tasks[i]["priority"]}')
        # kick back to menu
        todo()

    elif user_input == "q" or user_input == "Q":
        # exit app
        return print("Goodbye.")

    else:
        # kick back to menu if not one of the valid entries for this menu (1, 2, 3, q, and Q)
        print("Not a valid entry.")
        todo()

# call main function
todo()