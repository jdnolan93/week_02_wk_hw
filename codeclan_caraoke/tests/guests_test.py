import unittest
from src.songs import Songs
from src.guests import Guests

class TestGuests(unittest.TestCase):
    def setUp(self):
        self.guest = Guests("Jamie", "Africa by Toto", 100.0)

    def test_guest_has_name(self):
        self.assertEqual("Jamie", self.guest.name)

    def test_guest_has_fav_song(self):
        self.assertEqual("Africa by Toto", self.guest.fav_song)

    def test_guest_has_wallet(self):
        self.assertEqual(100.0, self.guest.wallet)


