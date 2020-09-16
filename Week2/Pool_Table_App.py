# a pool table management app which will manage the pool tables in University of Houston Center Games Room - one user, the admin. 
# To do:
    # Write to JSON
    # input validation

from datetime import datetime, date, time
import math

class Table():
    def __init__(self):
        self.occupied = False
        self.start = ""
        self.stop = ""
    
    # how long the tables have been occupied in minutes using datetime.now
    def total_minutes_elapsed(self):
        now = datetime.now()
        hours = now.strftime("%H")
        minutes = now.strftime("%M")
        x = int(hours) * 60
        y = int(minutes)
        minutes = x + y

        start_string = str(self.start)
        start_list = start_string.split(':')
        start_hours = int(start_list[0]) * 60
        start_minutes = int(start_list[1])
        start_total = start_hours + start_minutes

        total_time = minutes - start_total
        return total_time

    # total time played for file using stop property
    def time_played(self):
        stop_string = str(self.stop)
        stop_list = stop_string.split(':')
        stop_hours = int(stop_list[0]) * 60
        stop_minutes = int(stop_list[1])
        stop_total = stop_hours + stop_minutes
        
        start_string = str(self.start)
        start_list = start_string.split(':')
        start_hours = int(start_list[0]) * 60
        start_minutes = int(start_list[1])
        start_total = start_hours + start_minutes

        time_played = stop_total - start_total
        
        if time_played > 60:
            hours = math.floor(time_played / 60)
            minutes = time_played% 60
            return f"{hours} hours and {minutes} minutes."
        else:
            return f"{time_played} minutes."

    # cost in dollars
    def cost(self):
        total_time = self.total_minutes_elapsed()
        cost = total_time * rates_name.rate - rates_name.coupon
        return f"${cost}"

class Room():
    def __init__(self):
        self.tables = []

    # fills tables array with numbered tables
    def create_room(self, range_stop):
        for i in range(0, range_stop):
            name = i + 1
            name = Table()
            self.tables.append(name)

    # see all tables and whether they're occupied or not
    def print_table_list(self, room_name):
        for t in range(0, 12):
            if room_name.tables[t].occupied == True:
                print(f"Table {t + 1} - occupied")
            else:
                print(f"Table {t + 1} - unoccupied")
        
    
    # assign a table to a pool player
    def table_assign(self, index):
        if self.tables[index].occupied == True:
            print(f"Pool Table {index + 1} is currently occupied.")
            # print start time, time the table has been occupied
            print(f"Start Time: {room_name.tables[index].start}")

            total_time = room_name.tables[index].total_minutes_elapsed()
            # (hardmode: if >60, show in hours)
            if total_time > 60:
                hours = math.floor(total_time / 60)
                minutes = total_time % 60
                print(f"Total Time: {hours} hours and {minutes} minutes.")
            else:
                print(f"Total Time: {total_time} minutes.")
        else:
            self.tables[index].occupied = True
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            self.tables[index].start = time

# allows the admin to set different rates and apply coupons           
class Rates():
    def __init__(self):
        self.rate = .5
        self.coupon = 0

    def set_rate(self):
        # resets back to default when called
        self.rate = .5
        self. coupon = 0
        # different rates
        print("Default rate is $30/hr. Set a different rate? Y/N")
        conditional_response = input("> ")

        if conditional_response == "Y":
            response = input("What is the rate per hour for this player? ")
            self.rate = float(response) / 60     
        elif conditional_response == "N":
            self.rate = .5
        # coupons
        print("Does the player have any coupons? Y/N")
        coupon_exist = input("> ")

        if coupon_exist == "Y":
            self.coupon = int(input("Please enter the number of free minutes the player received: "))

# create a formatted file entry for a table
def table_entry(index):
    if room_name.tables[index].occupied == True:
        table_number = index + 1
        time_played = room_name.tables[index].time_played()
        cost = room_name.tables[index].cost()
    
        entry = f"""
            _________________________________________
            Table {table_number}
            Start Time - {room_name.tables[index].start}
            End Time - {room_name.tables[index].stop}
            Total Time Played - {time_played}
            Cost - {cost}
            ___________________________________________"""
    else:
        table_number = index + 1
        
        entry = f"""
            _________________________________________
            Table {table_number}
            Unoccupied
            ___________________________________________"""

    return entry

# creates a file name in the following format: (11-22-2017.txt or 11-22-2017.json)
def file_name():
    now = datetime.now()
    month = now.strftime("%m")
    day = now.strftime("%d")
    year = now.strftime("%Y")
    file_name = f"{month}-{day}-{year}.txt"
    return file_name

# writes a file to a file_name() with a table_entry() for every table
def file_write():
    this_file_name = file_name()
    with open(this_file_name, 'w') as new_file: 
        for i in range(0, len(room_name.tables)):
            entry = table_entry(i, )
            new_file.write(entry)

# calls all the functions needed when a table is closed out
def closeout(index):
    # assigns stop times to table being closed out
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    room_name.tables[index].stop = time
    # prompts the admin to set rates and coupons for this player
    rates_name.set_rate()
    # write file
    file_write()
    # print formatted cost for admin to tell player
    print(f"Player total: {room_name.tables[index].cost()}")

# instantiate a room
UH = Room()
# instantiate tables, passing the end of the range, so it can apply to any pool room
UH.create_room(13)
# setting instatiation name for Room class to variable name so the code doesn't change from pool room to pool room, and theoretically could run multiple at once
room_name = UH
# instantiate rates object
UH_rates = Rates()
# setting instatiation name for Rates class to variable name so the code doesn't change from pool room to pool room, and theoretically could run multiple at once
rates_name = UH_rates
# menu condition - does this need to be a global variable?
running = True

#menu
while running == True:
    print("""
        Press 1 to View All Tables. 
        Press 2 to Assign a Table.
        Press 3 to Closeout a Table. 
        Press Q to Quit.
    """)
    menu_select = input("> ")

    if menu_select == "1":
        room_name.print_table_list(room_name)

    elif menu_select == "2":
        table_input = input("Which table would you like to assign? ")
        index = int(table_input) - 1
        room_name.table_assign(index)

    elif menu_select == "3":
        closeout_input = input("Which table would you like to closeout? ")
        index = int(closeout_input) - 1
        closeout(index)
        
    elif menu_select == "Q" or menu_select == "q":
        print("Goodbye.")
        running = False

    else:
        print("Please enter 1, 2, 3, or Q/q.")
        
