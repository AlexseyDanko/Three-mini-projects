from pytube import YouTube
from art import tprint

# link = input('insert url:')
def download_audio(link=""):
    tprint('>>Download>>Audio>>function>>start>>', 'small')


def main():
    link = input('Please insert url: ')
    download_audio(link=link)
    url = YouTube(link)
    audio = url.streams.get_audio_only()
    tprint('Download process......', 'small')
    audio.download()
    tprint('>>>File>>>Uploaded>>>')


if __name__ == '__main__':
    main()
