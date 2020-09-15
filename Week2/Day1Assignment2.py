lists = []

def is_number(input_num):
    try:
        input_num = int(input_num)
        return True
    except ValueError:
        print("Whoops! That is not a valid number.")

class Shopping_list():
    def __init__(self, title, address):
        self.title = title
        self.address = address
        self.groceries = []
    
    def add_items(self, grocery_item):
        grocery_item.list_index = self

        if grocery_item not in self.groceries:
            self.groceries.append(grocery_item)

class Grocery_item():
    def __init__(self, title, cost, quantity, list_index):
        self.title = title
        self.cost = cost
        self.quantity = quantity
        self.list_index = list_index

def create_shopping_list():
    title = input("What would you like to name your list? ")
    address = input("Where will you be shopping? ")

    title = Shopping_list(title, address)
    lists.append(title)
    
    menu()

def view_all():
    print("-----All Lists-----")
    for l in range(0, len(lists)):
        print(f"{l} - {lists[l].title} - {lists[l].address}")
        
        for i in range(0, len(lists[l].groceries)):
            print(f"     {lists[l].groceries[i].title}")

    menu()

def menu_add_groceries():
    adding = True
    adding_input_no = ["N", "n", "no", "No"]
    
    print("-----List Indices-----")
    for l in range(0, len(lists)):
        print(f"{l} - {lists[l].title}")

    while adding == True:
        print("Would you like to add a new item? Y/N")
        adding_input = input("> ")
        
        if adding_input in adding_input_no:
            adding = False
            menu()

        else:
            index_str = input("Enter the index number of the list you'd like to add an item to. ")
    
            if is_number(index_str):
                index = int(index_str)
                if index < (len(lists)):
                    list_index = lists[index]
                    item_title = input("What do you need to buy? ")
                    item_cost = input("How much will it cost? ")
                    item_quantity = input("How many do you need? ")

                item_title = Grocery_item(item_title, item_cost, item_quantity, list_index)
                lists[index].add_items(item_title)

def menu():
    print("""
        Press 1 to Create a List. 
        Press 2 to Add an Item to a List.
        Press 3 to View All Lists. 
        Press Q to Quit.
    """)
    menu_select = input("> ")

    if menu_select == "1":
        create_shopping_list()

    elif menu_select == "2":
        menu_add_groceries()

    elif menu_select == "3":
        view_all()
        
    elif menu_select == "Q" or menu_select == "q":
        return print("Goodbye.")

    else:
        print("Please enter 1, 2, 3, or Q/q.")
        menu()

menu()