class Track:
    def __init__(self, name='', duration=0):
        self.__name = name
        self.__duration = duration

    def __str__(self):
        return f'{self.__name} - {self.__duration} min'

    def __add__(self, other):
        return str(self) + str(other)

    def __lt__(self, other):
        return self.__duration < other.__duration

    def __le__(self, other):
        return self.__duration <= other.__duration

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration


class Album:
    def __init__(self, name='', group=''):
        self.__name = name
        self.__group = group
        self.__tracks = []

    def __str__(self):
        result = 'Name group: ' + self.__name
        result += '\nName album: ' + self.__group
        result += '\nTracks:'
        if len(self.__tracks) < 1:
            result += '\nno tracks'
        else:
            for track in enumerate(self.__tracks, 1):
                result += f'\n      {track[0]}. {track[1]}'
        return result

    def __add__(self, other):
        return str(self) + str(other)

    def get_tracks(self):
        return [track for track in self.__tracks]

    def get_duration(self):
        result = 0
        for track in self.__tracks:
            result += track.__duration
        return result

    def add_track(self, track):
        if not isinstance(track, Track):
            raise NotImplementedError('Can not add this object to track list')
        self.__tracks.append(track)


albums = []
album = Album('The Fat of the Land', 'The Prodigy')
album.add_track(Track('Narayan', 9))
album.add_track(Track('Climbatize', 6))
album.add_track(Track('Breathe', 5))
albums.append(album)

album = Album('Опиум', 'Агата Кристи')
album.add_track(Track('Сказочная тайга', 2))
album.add_track(Track('Чёрная луна', 4))
album.add_track(Track('Трансильвания', 4))
albums.append(album)

for album in albums:
    print(album + '\n')

track1 = Track('Bohemian rhapsody', 6)
track2 = Track('The show must go on', 4)
print(track1 > track2)