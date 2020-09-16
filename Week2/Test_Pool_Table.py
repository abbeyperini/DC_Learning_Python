import unittest
from datetime import datetime
from Pool_Table_App import Room, Rates, Table

class PoolTests(unittest.TestCase):
    def setUp(self):
        self.test_room = Room()
        self.test_room.create_room(20)
        self.test_rates = Rates()
        print("Set up")

    def test_assign(self):
        room_name = self.test_room
        room_name.table_assign(5)
        room_name.table_assign(15)

    def test_print(self):
        room_name = self.test_room
        room_name.print_table_list(room_name)


unittest.main()