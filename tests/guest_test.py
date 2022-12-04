import unittest

from src.guest import Guest
# from src.water import Water

class TestGuest(unittest.TestCase):
    
    # Arrange -> Set up are data/classes so we can test 
    def setUp(self):
        self.guest = Guest('Tom Evans', 100)

    def test_guest_has_a_name (self):
        guest_has_name = self.guest.name
        self.assertEqual('Tom Evans', guest_has_name)

    