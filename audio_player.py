import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import pygame

class AudioPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Audio Player")
        self.root.geometry("600x400")

        self.file_path = None
        self.paused = False

        # Set up the mixer and initialize Pygame
        mixer.init()
        pygame.init()

        # Create a dictionary to store sound effects
        self.sound_effects = {}

        # Create a list to store the equalizer sliders
        self.equalizer_sliders = []

        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        # Create a frame for the title
        title_frame = tk.Frame(self.root, bg="#3498db")
        title_frame.pack(fill=tk.BOTH)

        # Create a title label
        title_label = tk.Label(title_frame, text="Audio Player", fg="white", bg="#3498db",
                               font=("Helvetica", 24, "bold"))
        title_label.pack(pady=10)

        # Create a frame for the file selection
        select_frame = tk.Frame(self.root)
        select_frame.pack(pady=10)

        # Create a select button
        select_button = tk.Button(select_frame, text="Select Audio", command=self.select_file,
                                  font=("Helvetica", 12, "bold"), bg="#3498db", fg="white")
        select_button.pack(side=tk.LEFT, padx=10)

        # Create a play button
        play_button = tk.Button(select_frame, text="Play", command=self.play,
                                font=("Helvetica", 12, "bold"), bg="#2ecc71", fg="white")
        play_button.pack(side=tk.LEFT, padx=10)

        # Create a pause button
        pause_button = tk.Button(select_frame, text="Pause", command=self.pause,
                                 font=("Helvetica", 12, "bold"), bg="#f1c40f", fg="white")
        pause_button.pack(side=tk.LEFT, padx=10)

        # Create a stop button
        stop_button = tk.Button(select_frame, text="Stop", command=self.stop,
                                font=("Helvetica", 12, "bold"), bg="#e74c3c", fg="white")
        stop_button.pack(side=tk.LEFT, padx=10)

        # Create a mute button
        mute_button = tk.Button(select_frame, text="Mute", command=self.toggle_mute,
                                font=("Helvetica", 12, "bold"), bg="#95a5a6", fg="white")
        mute_button.pack(side=tk.LEFT, padx=10)

        # Create a frame for the equalizer
        eq_frame = tk.Frame(self.root)
        eq_frame.pack(pady=20)

        # Create an equalizer label
        eq_label = tk.Label(eq_frame, text="Equalizer", font=("Helvetica", 16, "bold"))
        eq_label.pack()

        # Create equalizer sliders
        freq_bands = ["32 Hz", "64 Hz", "128 Hz", "256 Hz", "512 Hz"]
        for band in freq_bands:
            slider_frame = tk.Frame(eq_frame)
            slider_frame.pack(pady=10)

            label = tk.Label(slider_frame, text=band, font=("Helvetica", 12))
            label.pack(side=tk.LEFT, padx=10)

            slider = tk.Scale(slider_frame, from_=-10, to=10, orient=tk.HORIZONTAL, length=200, resolution=0.1,
                              command=self.update_equalizer)
            slider.set(0)  # Set default value to 0
            slider.pack(side=tk.LEFT)

            self.equalizer_sliders.append(slider)

        # Create a volume control frame
        volume_frame = tk.Frame(self.root)
        volume_frame.pack(pady=20)

        # Create a volume label
        volume_label = tk.Label(volume_frame, text="Volume", font=("Helvetica", 16, "bold"))
        volume_label.pack()

        # Create a volume slider
        volume_slider = tk.Scale(volume_frame, from_=0, to=100, orient=tk.HORIZONTAL, length=200,
                                 command=self.update_volume)
        volume_slider.set(50)  # Set default value to 50
        volume_slider.pack(pady=10)

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])

    def play(self):
        if self.file_path:
            if self.paused:
                mixer.music.unpause()
                self.paused = False
            else:
                mixer.music.load(self.file_path)
                mixer.music.play()

    def pause(self):
        if mixer.music.get_busy() and not self.paused:
            mixer.music.pause()
            self.paused = True

    def stop(self):
        if mixer.music.get_busy():
            mixer.music.stop()
            self.paused = False

    def toggle_mute(self):
        if mixer.music.get_volume() == 0.0:
            mixer.music.set_volume(0.5)
        else:
            mixer.music.set_volume(0.0)

    def update_equalizer(self, event):
        eq_values = [slider.get() for slider in self.equalizer_sliders]
        pygame.mixer.music.set_volume(0.5)  # Set the volume (0.0 to 1.0)
        pygame.mixer.music.set_equalizer(eq_values)

    def update_volume(self, event):
        volume = int(event)
        pygame.mixer.music.set_volume(volume / 100)

if __name__ == "__main__":
    player = AudioPlayer()
