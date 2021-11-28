class Room:
    def __init__(self, capacity, till):
        self.capacity = capacity
        self.till = till
        self.entry_fee = 2.0
        self.guests= []
        self.songs = []

    def count_songs(self):
        return len(self.songs)

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)
