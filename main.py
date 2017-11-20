import tkinter as tk
from tkinter import font
import serial
import threading
import time

ser = serial.Serial("COM5", baudrate=115200)

class Application(tk.Frame):
    def __init__ (self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.labeltop = tk.Label(self, text="HAHAHAHA")
        self.labeltop.grid(row = 0, column = 0, columnspan = 2, sticky = tk.W)

        self.labelpass = tk.Label(self, text="Password: ")
        self.labelpass.grid(row = 1, column = 0, sticky = tk.W)

        self.text = tk.Text(self, width = 20, height = 5, wrap = tk.WORD)
        self.text.grid(row = 3, column = 0, sticky = tk.W)

        self.quitButton = tk.Button(self, text="quit", command=self.quit)
        self.quitButton.grid(row=4, column = 0, sticky = tk.W)
    
class COMread(threading.Thread):
    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.appl = Application()
        self.daemon = True
        self.interval  = interval

    def run(self):
        while True:
            self.comdata = ser.read(4)
            self.appl.text.delete("0.0", tk.END)
            self.appl.text.insert("0.0", self.comdata)
            time.sleep(self.interval)

t = COMread(0.3)
app = t.appl
app.master.geometry("400x400")
app.master.title("sample")
t.start()   
app.mainloop()