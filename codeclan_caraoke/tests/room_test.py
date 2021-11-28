import unittest
from src.guests import Guests
from src.songs import Songs
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.test_room = Room(3, 50)

    def test_room_has_capacity(self):
        self.assertEqual(3, self.test_room.capacity)

    def test_room_has_till(self):
        self.assertEqual(50, self.test_room.till)