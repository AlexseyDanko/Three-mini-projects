import speech_recognition
import time

def main():
    rec = speech_recognition.Recognizer()
    microfone = speech_recognition.Microphone()
    unx_time = int(time.time())

    with microfone as source:
        rec.adjust_for_ambient_noise(source)
        print('Please speak text: ')
        audio = rec.listen(source)
    text = rec.recognize_google(audio, language='ru-RU')
    with open(f'{unx_time}.txt', 'w', encoding='utf-8') as file:
        file.write(text)
    print('File has been created: ')


if __name__ == '__main__':
    main()
