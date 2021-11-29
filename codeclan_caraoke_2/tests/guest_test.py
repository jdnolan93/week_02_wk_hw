import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Jamie", "Africa by Toto", 100.0)

    def test_guest_has_name(self):
        self.assertEqual("Jamie", self.guest_1.name)

    def test_guest_has_fav_song(self):
        self.assertEqual("Africa by Toto", self.guest_1.fav_song)

    def test_guest_has_wallet(self):
        self.assertEqual(100.0, self.guest_1.wallet)

    def test_money_leaves_wallet(self):
        self.guest_1.pay_admission(2)
        self.assertEqual(98, self.guest_1.wallet)