import unittest
from src.room import Room
from src.songs import Songs
from src.guests import Guests

class TestGuests(unittest.TestCase):
    def setUp(self):
        self.test_guest = Guests("Jamie", "Africa by Toto", 100.0)

    def test_guest_has_name(self):
        self.assertEqual("Jamie", self.test_guest.name)

    def test_guest_has_fav_song(self):
        self.assertEqual("Africa by Toto", self.test_guest.fav_song)

    def test_guest_has_wallet(self):
        self.assertEqual(100.0, self.test_guest.wallet)

