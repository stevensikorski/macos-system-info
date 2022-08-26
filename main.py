#!/usr/bin/env python3

from tkinter import *
from PIL import ImageTk, Image
from Foundation import NSBundle
from threading import Timer
import sys
import platform
import psutil

class Window:
    def __init__(self, window_width, window_height):
        if sys.platform != 'darwin':
            raise Exception(f'Incorrect platform, this application only runs on the latest macOS systems.')

        NSBundle.mainBundle().infoDictionary()['CFBundleName'] = 'macos-system-info'

        self.root = Tk()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))

        self.root.title('macos-system-info')
        self.root.call('wm', 'iconphoto', self.root._w, PhotoImage(file=f'{sys.path[0]}/images/icon.png'))
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        systemImage = ImageTk.PhotoImage(Image.open(f'{sys.path[0]}/images/iMac.png').resize((16, 16), Image.ANTIALIAS))
        siImage= ImageTk.PhotoImage(Image.open(f'{sys.path[0]}/images/logo.png').resize((16, 16), Image.ANTIALIAS))

        # System Information
        systemIcon = Label(self.root, image=systemImage, height=20, width=20)
        systemIcon.grid(row=0, column=0, padx=4, pady=4)
        systemTitle = Label(self.root, text='System Information', font=('Helvetica bold', 12))
        systemTitle.grid(row=0, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root, text="|", font=("Helvetica", 12))
        placeholder.grid(row=1, column=0, padx=0, pady=4)
        systemText = Label(self.root, text=f'System: {platform.uname().system}', font=('Helvetica', 12))
        systemText.grid(row=1, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root, text="|", font=("Helvetica", 12))
        placeholder.grid(row=2, column=0, padx=0, pady=4)
        nodeText = Label(self.root, text=f'Node: {platform.uname().node}', font=('Helvetica', 12))
        nodeText.grid(row=2, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root, text="|", font=("Helvetica", 12))
        placeholder.grid(row=3, column=0, padx=0, pady=4)
        releaseText = Label(self.root, text=f'Release: {platform.uname().release}', font=('Helvetica', 12))
        releaseText.grid(row=3, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root, text="|", font=("Helvetica", 12))
        placeholder.grid(row=4, column=0, padx=0, pady=4)
        versionText = Label(self.root, text=f'Version: {platform.uname().version}', font=('Helvetica', 12))
        versionText.grid(row=4, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root, text="|", font=("Helvetica", 12))
        placeholder.grid(row=5, column=0, padx=0, pady=4)
        machineText = Label(self.root, text=f'Machine: {platform.uname().machine}', font=('Helvetica', 12))
        machineText.grid(row=5, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root)
        placeholder.grid(row=6, column=0, padx=4, pady=4)

        # Processor Information
        cpuIcon = Label(self.root, image=siImage, height=20, width=20)
        cpuIcon.grid(row=7, column=0, padx=4, pady=4)
        cpuTitle = Label(self.root, text='Processor Information', font=('Helvetica bold', 12))
        cpuTitle.grid(row=7, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root, text="|", font=("Helvetica", 12))
        placeholder.grid(row=8, column=0, padx=0, pady=4)
        processorText = Label(self.root, text=f'Processor: {platform.uname().processor}', font=('Helvetica', 12))
        processorText.grid(row=8, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root, text="|", font=("Helvetica", 12))
        placeholder.grid(row=9, column=0, padx=0, pady=4)
        physicalText = Label(self.root, text=f'Physical Cores: {psutil.cpu_count(logical=False)}', font=('Helvetica', 12))
        physicalText.grid(row=9, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root, text="|", font=("Helvetica", 12))
        placeholder.grid(row=10, column=0, padx=0, pady=4)
        totalText = Label(self.root, text=f'Total Cores: {psutil.cpu_count(logical=True)}', font=('Helvetica', 12))
        totalText.grid(row=10, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root, text="|", font=("Helvetica", 12))
        placeholder.grid(row=11, column=0, padx=0, pady=4)
        usageText = Label(self.root, text=f'Usage: {psutil.cpu_percent()}%', font=('Helvetica', 12))
        usageText.grid(row=11, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root)
        placeholder.grid(row=12, column=0, padx=4, pady=4)

        # Memory Information
        memoryIcon = Label(self.root, image=siImage, height=20, width=20)
        memoryIcon.grid(row=13, column=0, padx=4, pady=4)
        memoryTitle = Label(self.root, text='Memory Information', font=('Helvetica bold', 12))
        memoryTitle.grid(row=13, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root, text="|", font=("Helvetica", 12))
        placeholder.grid(row=14, column=0, padx=0, pady=4)
        totalText = Label(self.root, text=f'Total: {psutil.virtual_memory().percent}%', font=('Helvetica', 12))
        totalText.grid(row=14, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root)
        placeholder.grid(row=15, column=0, padx=4, pady=4)

        # Battery Information

        batteryIcon = Label(self.root, image=siImage, height=20, width=20)
        batteryIcon.grid(row=16, column=0, padx=4, pady=4)
        batteryTitle = Label(self.root, text='Battery Information', font=('Helvetica bold', 12))
        batteryTitle.grid(row=16, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root, text="|", font=("Helvetica", 12))
        placeholder.grid(row=17, column=0, padx=0, pady=4)
        totalText = Label(self.root, text=f'Total: {psutil.sensors_battery().percent}%', font=('Helvetica', 12))
        totalText.grid(row=17, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root, text="|", font=("Helvetica", 12))
        placeholder.grid(row=18, column=0, padx=0, pady=4)
        totalText = Label(self.root, text=f'Plugged: {psutil.sensors_battery().power_plugged}', font=('Helvetica', 12))
        totalText.grid(row=18, column=1, padx=0, pady=4, sticky=W)

        placeholder = Label(self.root, text="|", font=("Helvetica", 12))
        placeholder.grid(row=19, column=0, padx=0, pady=4)
        totalText = Label(self.root, text=f'Left: {psutil.sensors_battery().secsleft / 60} minutes', font=('Helvetica', 12))
        totalText.grid(row=19, column=1, padx=0, pady=4, sticky=W)

        self.root.mainloop()

def main():
    Container = Window(800, 600)

if __name__ == "main":
    main()