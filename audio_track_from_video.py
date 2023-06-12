import moviepy.editor
from art import tprint


def cut_out_audio(video_file=""):
    tprint('Download Cut_out_Audio function start', 'small')
    video = moviepy.editor.VideoFileClip(f'{video_file}')
    audio = video.audio
    audio.write_audiofile(f'{video_file}.mp3')


def main():
    cut_out_audio(video_file=input('Please insert path file avi: '))


if __name__ == '__main__':
    main()
