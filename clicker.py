from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import time
import threading


trigger = KeyCode(char='s')
click = False
mouse = Controller()


def clicker():
    while True:
        if click:
            mouse.click(Button.left, 1)
            time.sleep(0.1)


def event(key):
    if key == trigger:
        global click
        click = not click


def main():
    clicking_thread = threading.Thread(target=clicker)
    clicking_thread.start()

    with Listener(on_press=event) as listener:
        listener.join()


if __name__ == '__main__':
    main()
