import tkinter as tk
import os

class Window:
    def __init__(self, width, height):
        self.root = tk.Tk()

        window_width = width
        window_height = height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))

        self.root.title('os-system-info')
        self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file='images/icon.png'))
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        self.root.mainloop()

Window(800, 500)