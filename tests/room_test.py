import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song('Dancing Queen')
        self.song_2 = Song('Under Pressure')
        self.song_3 = Song('Bohemian Rapsody')
        self.song_4 = Song ('Halleluiah')
        self.song_5 = Song ('We are young')
        self.guest_1 = Guest('Tom Evans')
        self.guest_2 = Guest('Cathy Jones')
        self.guest_3 = Guest('Jeff Mendes')
        
        guest_list = [self.guest_1, self.guest_2]
        song_list = [self.song_1, self.song_2]

        self.room = Room (1, song_list, guest_list, 12)

    def test_room_has_capacity (self):
        room_capacity = self.room.room_has_capacity()
        self.assertEqual(12, room_capacity)

    def test_length_of_guest_list (self):
        list_length = self.room.length_of_guest_list()
        self.assertEqual(2, list_length)
    
    def test_room_can_check_in_guest (self):
        self.room.room_can_check_in_guest(self.guest_3)
        self.assertEqual(3, len(self.room.guest_list))
    
    def test_room_can_check_out_guest (self):
        self.room.room_can_check_out_guest(self.guest_1)
        self.assertEqual(1, len(self.room.guest_list))
    
    def test_room_can_add_song (self):
        self.room.room_can_add_song(self.song_3)
        self.assertEqual(3, len(self.room.song_list))


    


        # Check room has capacity
        # check how many guests has the room got?
        # check if you can check-in any more( capacity>guests)
        # function to remove guests
        # function to add songs to room

        # list_of_rooms = [
        #     {'number' : 1, 'capacity': 4, 'list of guests' : [self.guest_1, self.guest_2], 'list of songs' : [self.song_1, self.song_2]},
        #     {'number' : 2, 'capacity': 8, 'list of guests' : [], 'list of songs' : []}, 
        #     {'number' : 3, 'capacity': 12, 'list of guests' : [], 'list of songs' : []}
        #     ]
        # self.list_of_rooms = Room(list_of_rooms)
        
    
    # def test_bar_can_add_rooms (self):
    #     self.rooms.bar_can_add_rooms(self.rooms.append({'number' : 4, 'capacity': 12, 'list of guests' : [], 'list of songs' : []}))
    #     self.assertEqual(4, len(self.list_of_rooms))
    # def test_room_has_space (self):
    #     self.list_of_rooms.room_has_space()
    #     self.assertEqual(self.list_of_rooms['capacity'] > len(self.list_of_rooms['list_of_guests']))

    
    # def test_room_can_add_song (self):
    #     self.room_1.room_can_add_song(self.song_4)
    #     self.assertEqual(4, len(self.room_1.list_of_songs))
    
    # def test_room_can_add_song_1 (self):
    #     self.room_2.room_can_add_song(self.song_5)
    #     self.assertEqual(4, len(self.room_2.list_of_songs)) #how to add mnore than one song at a time?
    
    # def test_room_can_check_in_guest (self):
    #     self.room_1.room_can_add_guest(self.guest_1)
    #     self.assertEqual(1, len(self.room_1.list_of_guests))


    # def test_room_can_check_out_guest (self):
    #     self.room_1.room_can_remove_guest(self.guest_1)
    #     self.assertEqual(0, len(self.room_1.list_of_guests))


        



    
