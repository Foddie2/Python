import yt_dlp

URL = input('Enter URL: ')
yt_opts = {}

with yt_dlp.YoutubeDL(yt_opts) as ydl:
    ydl.download([URL])
    
print('Video downloaded successfully')