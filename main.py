import tkinter as tk
from tkinter import font
import serial
import threading
import time

#ser = serial.Serial("COM5", baudrate=115200)
logfile = open("c:\\files\\project_master\\log.txt", "rb+")

class Application(tk.Frame):
    def __init__ (self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):

        self.labelpass = tk.Label(self, font=("Impact", 20), foreground = "red", text="Current value: ")
        self.labelpass.grid(row = 1, column = 0, sticky = tk.W)

        self.text = tk.Text(self, bd = 0, font=("Impact", 25),  width = 5, height = 1, wrap = tk.WORD)
        self.text.grid(row = 1, column = 2, sticky = tk.E)

        self.quitButton = tk.Button(self, font=("Impact", 14), text="quit", command=self.quit)
        self.quitButton.grid(row=3, column = 0, sticky = tk.W)
    
class COMread(threading.Thread):
    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.appl = Application()
        self.daemon = True
        self.interval  = interval

    def run(self):
        while True:
            self.comdata = logfile.readlines()[-1]
            self.appl.text.delete("0.0", tk.END)
            self.appl.text.insert("0.0", self.comdata)
            time.sleep(self.interval)

t = COMread(0.1)
app = t.appl
app.master.geometry("400x400")
app.master.title("sample")
t.start()   
app.mainloop()