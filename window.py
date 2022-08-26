from tkinter import * 
import sys
from sys import platform
from Foundation import NSBundle

class Window:
    def __init__(self, window_width, window_height):
        if platform != 'darwin':
            raise Exception('Incorrect platform, this application only runs on the latest macOS systems')

        NSBundle.mainBundle().infoDictionary()['CFBundleName'] = 'macos-system-info'

        self.root = Tk()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))

        self.root.title('macos-system-info')
        self.root.call('wm', 'iconphoto', self.root._w, PhotoImage(file=f'{sys.path[0]}/images/icon.png'))
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    def mainLoop(self):
        self.root.mainloop()

    def createLabel(self, text, column, row, padx, pady):
        label = Label(self.root, text=text, padx=padx, pady=pady)
        label.grid(column=column, row=row)

Container = Window(800, 500)
Label1 = Container.createLabel("text1", 0, 0, 5, 5)
Label2 = Container.createLabel("text2", 0, 1, 5, 5)
Container.mainLoop()
