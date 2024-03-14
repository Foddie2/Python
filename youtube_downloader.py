import pytube

link = input('Enter Youtube Video URL: ')
video_download = pytube.YouTube(link)
video_download.streams.first().download()
print('Video Downloaded', link)