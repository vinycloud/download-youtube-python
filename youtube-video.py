from pytube import YouTube

# type de URL of Youtube video and type the directory to save #
link = input("Enter your Youtube Video URL: ")
path = input("Enter your directory to save: ")
yt = YouTube(link)

# Show the details of video #
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Size of video: ", yt.length, "segundos")
print("Evaluation of video: ", yt.rating)

# Use the highest resolution #
def new_func(yt):
    ys = yt.streams.get_highest_resolution()
    return ys
ys = new_func(yt)

# Starting download video #
print("Downloading...")
ys.download(path)
print("Download completed!")