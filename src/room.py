class Room():
    def __init__(self, room_number, song_list, guest_list, capacity):
        self.room_number = room_number
        self.song_list = song_list
        self.guest_list = guest_list
        self.capacity = capacity

    
    def room_has_capacity (self):
        return self.capacity

    def length_of_guest_list (self):
        return len(self.guest_list)

    def room_can_check_in_guest (self, guest):
            if self.capacity > len(self.guest_list):
                self.guest_list.append(guest)
            else:
                return "Sorry, we're fully booked"
    
    def room_can_check_out_guest (self, guest):
        self.guest_list.remove(guest)

    def room_can_add_song (self, song):
        self.song_list.append(song)

        # # self.room_number = room_number
        # self.fully_booked = False
        # self.list_of_rooms = list_of_rooms


    # def room_has_space (self, room):
    #     for room in self.list_of_rooms:
    #         if room['capacity'] > len(room['list_of_guests']):
    #             return f" You may check in"
    #     else:
    #         return f"Sorry, we're fully booked"



    # def bar_can_add_rooms (self, room):
    #     self.list_of_rooms.append(room)
    
    # def room_can_add_guest (self, guest):
    #     self.list_of_guests.append(guest)

    # def room_can_remove_guest (self, guest):
    #     self.list_of_guests.remove(guest)

        

    

