from pytube import YouTube
from art import tprint

# link = input('insert url:')
def download_video(link=""):
    tprint('>>Download>>Video>>function>>start>>', 'small')


def main():
    link = input('Please insert url: ')
    download_video(link=link)
    url = YouTube(link)
    video = url.streams.get_highest_resolution()
    tprint('Download process......', 'small')
    video.download()
    tprint('>>>File>>>Uploaded>>>')


if __name__ == '__main__':
    main()


