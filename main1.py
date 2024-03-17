import pytube

url = input("Enter Video Url to download: ")

yt = pytube.YouTube(url)

print("Video Dowloading...")

stream = yt.streams.get_lowest_resolution()

stream.download()

print("Video Dowloaded!")