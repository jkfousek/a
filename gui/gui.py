import tkinter as tk
from tkinter import messagebox

# Function to display the entered text
def show_message():
    user_text = entry.get()
    if user_text:
        messagebox.showinfo("Message", f"You entered: {user_text}")
    else:
        messagebox.showwarning("Warning", "Please enter some text!")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("300x200")  # Set window size (width x height)

# Create a label
label = tk.Label(root, text="Enter something:", font=("Arial", 12))
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Create a button
button = tk.Button(root, text="Show Message", command=show_message, font=("Arial", 12))
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
import tkinter as tk
from tkinter import ttk
import os
import sys
import subprocess
import time

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My GUI")
        self.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Hello, Tkinter!")
        label.pack(pady=20)
        button = ttk.Button(self, text="Click Me", command=self.on_button_click)
        button.pack(pady=10)

    def on_button_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Starting virtual display.")
        try:
            xvfb_proc = subprocess.Popen(['Xvfb', ':1', '-screen', '0', '1024x768x24'])
            os.environ['DISPLAY'] = ':1'
            time.sleep(2)  # Wait for Xvfb to start
            vnc_proc = subprocess.Popen(['x11vnc', '-display', ':1', '-nopw', '-listen', 'localhost', '-xkb'])
        except FileNotFoundError:
            print("Xvfb or x11vnc not found. Please install them to run in headless mode.")
            sys.exit(1)
    app = GUI()
    app.mainloop()
    if 'xvfb_proc' in locals():
        xvfb_proc.terminate()
    if 'vnc_proc' in locals():
        vnc_proc.terminate()
