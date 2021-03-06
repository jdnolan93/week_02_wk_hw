class Room:
    def __init__(self, capacity, till):
        self.capacity = capacity
        self.till = till
        self.admission_fee = 2.0
        self.guests = []
        self.songs = []

    def count_songs(self):
        return len(self.songs)

    def add_song(self, song):
        self.songs.append(song)

    # def remove_song(self, song):
        # self.songs.remove(song)    #Realised there would be problem if song wasn't in list

    def remove_song(self, song):
        for song_to_remove in self.songs:
            if song_to_remove == song:
                self.songs.remove(song)

    def count_guests(self):
        return len(self.guests)

    def add_guest(self, guest):
        capacity = 3
        if len(self.guests) < capacity:
             self.guests.append(guest)
        else:
            return "Sorry, we're full!"

    # def remove_guest(self, guest):  #Realised there would be problem if guest wasn't in list
    #     self.guests.remove(guest)

    def remove_guest(self, guest):
        for guest_to_remove in self.guests:
            if guest_to_remove == guest:
                self.guests.remove(guest)

    def take_admission_fee(self, guest, fee):
        if guest.wallet >= fee:
            guest.pay_admission(fee)
            self.till += fee

    
        