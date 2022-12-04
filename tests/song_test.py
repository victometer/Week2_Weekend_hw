import unittest

from src.song import Song
# from src.water import Water

class TestSong(unittest.TestCase):
    
    # Arrange -> Set up are data/classes so we can test 
    def setUp(self):
        self.song = Song('Survivor')

    def test_song_has_a_name (self):
        song_has_name = self.song.name
        self.assertEqual('Survivor', song_has_name)
