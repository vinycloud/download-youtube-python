from pytube import Playlist

# type de URL of Youtube Playlist and type the directory to save #
link = input('Enter Youtube Playlist URL: ')
path = input('Enter directory to save: ')
yt_playlist = Playlist(link)

# Use the highest resolution #
for video in yt_playlist.videos:
    video.streams.get_highest_resolution().download(path)
    print('Video Downloaded: ', video.title)
print('\nAll videos are downloaded.')  