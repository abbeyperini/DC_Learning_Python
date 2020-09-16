# a pool table management app which will manage the pool tables in University of Houston Center Games Room - one user, the admin. 
# MORE HARD MODE - Write Unit Tests for your application
# MORE HARD MODE - different cost for students, teachers, and coupons

from datetime import datetime, date, time

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

    def cost(self):
        # $30 per hour/50 cents a min
        total_time = self.total_minutes_elapsed()
        cost = total_time * .5
        return cost
        # cost in $$$

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
        return time_played

class Room():
    def __init__(self):
        self.tables = []

    # fills tables array with 12 numbered tables
    def create_room(self):
        # MAKE IT SO THE STOP OF THIS RANGE IS SET WHEN THE ROOM IS INSTANTIATED
        for i in range(0, 13):
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
                total_time /= 60
                # NO FLOAT - HOURS AND MINUTES?
                # update file print when this gets figured out ^
                print(f"Total Time: {total_time} hours.")
            else:
                print(f"Total Time: {total_time} minutes.")
        else:
            self.tables[index].occupied = True
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            self.tables[index].start = time
        

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
            Total Time Played - {time_played} minutes
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

def file_name():
    # The file should be named in the following format: (11-22-2017.txt or 11-22-2017.json)
    now = datetime.now()
    month = now.strftime("%m")
    day = now.strftime("%d")
    year = now.strftime("%Y")
    file_name = f"{month}-{day}-{year}.txt"
    return file_name

def file_write():
    this_file_name = file_name()
    with open(this_file_name, 'w') as new_file: 
        for i in range(0, len(room_name.tables)):
            entry = table_entry(i)
            new_file.write(entry)
    new_file.close()

def closeout(index):
    # assign stop to table
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    room_name.tables[index].stop = time
    # write file
    file_write()
    # return formatted cost
    print(room_name.tables[index].cost())

UH = Room()
UH.create_room()
room_name = UH
running = True

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
        
