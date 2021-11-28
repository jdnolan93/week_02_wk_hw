import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.test_songs = Song("Africa by Toto")

    def test_song_has_title(self):
        self.assertEqual("Africa by Toto", self.test_songs.title)
