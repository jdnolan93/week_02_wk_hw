class Guest:
    def __init__(self, name, fav_song, wallet):
        self.name = name
        self.fav_song = fav_song
        self.wallet = wallet

    def pay_admission(self, amount):
        self.wallet -= amount