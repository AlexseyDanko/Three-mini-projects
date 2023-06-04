from pytube import YouTube


link = input('insert url:')

url = YouTube(link)

video = url.streams.get_highest_resolution()
video.download()


# audio = url.streams.get_audio_only()
# audio.download()




