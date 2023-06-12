from pytube import YouTube
from art import tprint


def download_audio(link=""):
    tprint('>>Download>>Audio>>function>>start>>', 'small')
    url = YouTube(link)
    audio = url.streams.get_audio_only()
    tprint('Download process......', 'small')
    audio.download()
    tprint('>>>File>>>Uploaded>>>')


def main():
    download_audio(link=input('Please insert url: '))


if __name__ == '__main__':
    main()
