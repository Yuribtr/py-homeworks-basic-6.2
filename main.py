class Track:
    def __init__(self, name='', duration=0):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'{self.name} - {self.duration} min'

    def __add__(self, other):
        return str(self) + str(other)

    def __lt__(self, other):
        return self.duration < other.duration

    def __le__(self, other):
        return self.duration <= other.duration

    def set_name(self, name):
        self.name = name

    def set_duration(self, duration):
        self.duration = duration


class Album:
    def __init__(self, name='', group=''):
        self.name = name
        self.group = group
        self.tracks = []

    def __str__(self):
        result = 'Name group: ' + self.name
        result += '\nName album: ' + self.group
        result += '\nTracks:'
        if len(self.tracks) < 1:
            result += '\nno tracks'
        else:
            for track in enumerate(self.tracks, 1):
                result += f'\n      {track[0]}. {track[1]}'
        return result

    def __add__(self, other):
        return str(self) + str(other)

    def get_tracks(self):
        return [track for track in self.tracks]

    def get_duration(self):
        result = 0
        for track in self.tracks:
            result += track.duration
        return result

    def add_track(self, track):
        if not isinstance(track, Track):
            raise NotImplementedError('Can not add this object to track list')
        self.tracks.append(track)


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
    # print(f'Альбом "{album.name}" группы {album.group}:')
    # for track in enumerate(album.get_tracks(), 1):
    #     print(f'{track[0]}. {track[1]}')
    # print(f'Общая длительность альбома: {album.get_duration()} минут\n')

track1 = Track('Bohemian rhapsody', 6)
track2 = Track('The show must go on', 4)
print(track1 > track2)