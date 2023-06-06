from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length, "seconds")

yd = yt.streams.get_highest_resolution()

print("Downloading...")


yd.download(
    # the path where the video will be downloaded
)

print("Download completed!!")
