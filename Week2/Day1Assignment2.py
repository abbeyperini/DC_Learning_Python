lists = []

def is_number(input_num):
    try:
        input_num = int(input_num)
        return True
    except ValueError:
        print("Whoops! That is not a valid number.")

class shopping_list():
    def __init__(self, title, address):
        self.title = title
        self.address = address
        self.groceries = []

    def add_groceries(self):
        item_title = input("What do you need to buy? ")
        item_cost = input("How much will it cost? ")
        item_quantity = input("How many do you need? ")

        item_title = {"title": item_title, "cost": item_cost, "quantity": item_quantity}
        self.groceries.append(item_title)
        
        menu()

def create_shopping_list():
    title = input("What would you like to name your list? ")
    address = input("Where will you be shopping? ")

    title = shopping_list(title, address)
    lists.append(title)
    
    menu()

def view_all():
    print("-----All Lists-----")
    for l in range(0, len(lists)):
        print(f"{l} - {lists[l].title} - {lists[l].address}")
        
        for i in range(0, len(lists[l].groceries)):
            print(f"     {lists[l].groceries[i]['title']}")

    menu()

def menu_add_groceries():
    print("-----List Indices-----")
    for l in range(0, len(lists)):
        print(f"{l} - {lists[l].title}")
        
    index_str = input("Enter the index number of the list you'd like to add. ")
    
    if is_number(index_str):
        index = int(index_str)
        if index < (len(lists)):
            lists[index].add_groceries()
        else:
            print("Not a valid index number.")
            menu()
    else:
        print("Not a valid number.")
        menu()

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