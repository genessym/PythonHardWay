class Song:
    
    def __init__(self, name, lyrics, artist):
        self.name = name
        self.lyrics = lyrics
        self.artist = artist
    
    def beginning_lyric(self):
        return "The song begins with \'{}\'".format(self.lyrics)

                 
happy_bday = Song("Happy Birthday to you...","Birthday people")
             
bulls_on_parade = Song("They rally around the family...", "The Bulls")
                    
print(bulls_on_parade.artist)
print(happy_bday.artist)

#happy_bday.sing_me_a_song()
#bulls_on_parade.sing_me_a_song()
#Song.sing_me_a_song(happy_bday)
#print(happy_bday.sing_me_a_song)