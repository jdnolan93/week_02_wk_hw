import unittest
from src.room import Room
from src.guests import Guests
from src.songs import Songs

class TestSongs(unittest.TestCase):
    def setUp(self):
        self.test_songs = Songs("Africa by Toto")

    def test_song_has_title(self):
        self.assertEqual("Africa by Toto", self.test_songs.title)

