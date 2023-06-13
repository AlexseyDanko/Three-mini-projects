import speech_recognition
import time


def main():
    r = speech_recognition.Recognizer()
    file = speech_recognition.AudioFile(input('please insert path to the file: '))
    unx_time = int(time.time())
    print('Processing...')
    with file as source:
        r.adjust_for_ambient_noise(source)
        file = r.record(source)
        result = r.recognize_google(file, language='ru-RU')
        # print(result)
    with open(f'{unx_time}.txt', 'w', encoding='utf-8') as file:
        file.write(result)


if __name__ == '__main__':
    main()
