import tkinter as tk
import time
import threading
#pip install pyautogui
class AutoClickerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AutoClicker")
        self.root.geometry("200x200")

        self.click_interval = 1000  # Интервал между кликами (в миллисекундах)
        self.running = False

        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        # Создаем метку для отображения информации о состоянии
        self.status_label = tk.Label(self.root, text="Status: Stopped", font=("Helvetica", 12))
        self.status_label.pack(pady=10)

        # Создаем скролл для изменения интервала между кликами
        self.interval_scale = tk.Scale(self.root, from_=100, to=2000, resolution=100, orient=tk.HORIZONTAL,
                                       label="Interval (ms)", font=("Helvetica", 10), length=150, showvalue=0,
                                       command=self.update_interval)
        self.interval_scale.set(self.click_interval)
        self.interval_scale.pack(pady=10)

        # Создаем кнопку "Start"
        self.start_button = tk.Button(self.root, text="Start", command=self.start_auto_click,
                                      font=("Helvetica", 12), bg="#2ecc71", fg="white")
        self.start_button.pack()

        # Создаем кнопку "Stop"
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_auto_click,
                                     font=("Helvetica", 12), bg="#e74c3c", fg="white")
        self.stop_button.pack(pady=10)

    def start_auto_click(self):
        if not self.running:
            self.running = True
            self.status_label.config(text="Status: Running")
            threading.Thread(target=self.auto_click).start()

    def stop_auto_click(self):
        if self.running:
            self.running = False
            self.status_label.config(text="Status: Stopped")

    def update_interval(self, event):
        self.click_interval = self.interval_scale.get()
    def auto_click(self):
        while self.running:
            try:
                import pyautogui
                pyautogui.click()
            except ImportError:
                print("pyautogui library is not installed. Please install it using 'pip install pyautogui'.")

            time.sleep(self.click_interval / 1000)  # Пауза между кликами

if __name__ == "__main__":
    app = AutoClickerApp()
