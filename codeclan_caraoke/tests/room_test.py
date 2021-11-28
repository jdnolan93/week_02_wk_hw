import unittest
from src.guests import Guests
from src.songs import Songs
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.test_room = Room(3, 50)
        self.guest_1 = Guests("Poor Joe", "Barbie Girl by Aqua", 1.0)
        self.guest_2 = Guests("Richie Ritch", "Money, Money, Money by Abba", 9999.9)
        self.guest_3 = Guests("Basic Beth", "Mr Brightside by The Killers", 50.0)
        self.guest_4 = Guests("Overcapacity Oscar", "Let Me In by The Sensations", 9.0)
        self.song_1 = Songs("One More Time by Daft Punk")
        self.song_2 = Songs("Africa by Toto")
        self.song_3 = Songs("Mr Brightside by The Killers")
        self.song_4 = Songs("Barbie Girl by Aqua")
        self.song_5 = Songs("All Star by Smash Mouth")
        self.song_6 = Songs("Clint Eastwood by Gorillaz")

    def test_room_has_capacity(self):
        self.assertEqual(3, self.test_room.capacity)

    def test_room_has_till(self):
        self.assertEqual(50, self.test_room.till)

    def test_add_song(self):
        self.room_test.add_song(self.song_5)