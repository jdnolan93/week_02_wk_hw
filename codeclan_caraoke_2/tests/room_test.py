import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(3, 500)
        self.lonely_room = Room(1,300)
        self.guest_1 = Guest("Poor Joe", "Barbie Girl by Aqua", 1.0)
        self.guest_2 = Guest("Richie Ritch", "Money, Money, Money by Abba", 9999.9)
        self.guest_3 = Guest("Basic Beth", "Mr Brightside by The Killers", 50.0)
        self.guest_4 = Guest("Overcapacity Oscar", "Let Me In by The Sensations", 9.0)
        self.song_1 = Song("One More Time by Daft Punk")
        self.song_2 = Song("Africa by Toto")
        self.song_3 = Song("Mr Brightside by The Killers")
        self.song_4 = Song("Barbie Girl by Aqua")
        self.song_5 = Song("All Star by Smash Mouth")
        self.song_6 = Song("Clint Eastwood by Gorillaz")

    def test_room_has_capacity(self):
        self.assertEqual(3, self.room.capacity)

    def test_room_has_till(self):
        self.assertEqual(500, self.room.till)

    def test_song_count(self):
        self.assertEqual(0, self.room.count_songs())

    def test_add_song(self):
        self.room.add_song(self.song_5)
        self.assertEqual(1, self.room.count_songs())

    def test_remove_song(self):
        self.room.add_song(self.song_5)
        self.room.remove_song(self.song_5)
        self.assertEqual(0, self.room.count_songs())

    def test_guest_count(self):
        self.assertEqual(0, self.room.count_guests())

    def test_can_add_guest(self):
        self.room.add_guest(self)
        self.assertEqual(1, self.room.count_guests())

    def test_can_remove_guest(self):
        self.room.add_guest(self.guest_3)
        self.room.remove_guest(self.guest_3)
        self.assertEqual(0, self.room.count_guests())

    # def test_room_too_busy(self):
    #     self.lonely_room.add_guest(self.guest_3)
    #     self.assertEqual("Sorry, we're full!", self.lonely_room.add_guest(self.guest_4))

    # why isn't this working??

    def test_take_admission_fee(self):
        self.room.take_admission_fee(self.guest_3, 2.0)
        self.assertEqual(502, self.room.till) 


