class Room():
    def __init__(self, room_number, song_list, guest_list, capacity, fee):
        self.room_number = room_number
        self.song_list = song_list
        self.guest_list = guest_list
        self.capacity = capacity
        self.fee = fee

    
    def room_has_capacity (self):
        return self.capacity

    def length_of_guest_list (self):
        return len(self.guest_list)

    # def room_can_check_in_guest (self, guest):
    #         if self.capacity > len(self.guest_list):
    #             self.guest_list.append(guest)
    #         else:
    #             return "Sorry, we're fully booked"
    
    def room_can_check_in_guest (self, guest):
            if self.capacity > len(self.guest_list):
                self.guest_list.append(guest)          
                
    def room_has_space(self, guest):
        while self.capacity > len(self.guest_list):
            self.capacity -= len(self.guest_list)
            return self.room_can_check_in_guest(guest)
        else:
            return 'Sorry, the room is full'
    
    def room_can_check_out_guest (self, guest):
        self.guest_list.remove(guest)

    def room_can_add_song (self, song):
        self.song_list.append(song)

    def guest_can_pay_fee(self, guest_money):
        if guest_money >= self.fee:
            return 'Welcome'
        return 'Sorry, not enough funds'

    def guest_has_favourite_song (self, song_name):
        for song in self.song_list:
            if song.name == song_name:
                return 'Whoo'
    

        

    

