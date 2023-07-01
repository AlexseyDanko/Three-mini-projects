from pytube import YouTube
from art import tprint


def download_video(link=""):
    tprint('>>Download>>Video>>function>>start>>', 'small')
    url = YouTube(link)
    video = url.streams.get_highest_resolution()
    tprint('Download process......', 'small')
    video.download()
    tprint('>>>File>>>Uploaded>>>')


def main():
    download_video(link=input('Please insert url: '))


if __name__ == '__main__':
    main()
