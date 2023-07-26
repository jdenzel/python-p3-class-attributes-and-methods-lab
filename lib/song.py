class Song:
    
    count = 0
    genres = []
    genre_count = {}
    artists = []
    artist_count = {}

    

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)


    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    def add_to_genres(self, genre):
        if genre not in self.genres:
            self.genres.append(genre)

    def add_to_artists(self, artist):
        if artist not in self.artists:
            self.artists.append(artist)

    def add_to_genre_count(self, genre):
        if genre not in self.genre_count:
            self.genre_count[genre] = 1
        else:
            self.genre_count[genre] += 1

    def add_to_artist_count(self, artist):
        if artist not in self.artist_count:
            self.artist_count[artist] = 1
        else:
            self.artist_count[artist] += 1
