import tkinter as tk
from tkinter import font
import threading
from threading import Thread, Lock
import time
import serial

ser = serial.Serial("COM5", baudrate=115200)
#logfile = open("c:\\files\\project_master\\log.txt", "rb+")
lock = threading.Lock()

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

def COMread():
    while True:
        lock.acquire()
        try:
            logfile = open("c:\\files\\project_master\\log.txt", "a")
            received = ser.readline(4)
            strdata = str(received)
            logfile.writelines(strdata + "\n")
            logfile.close()
        finally:
            lock.release()
app = Application()

def Write():
    while True:
        lock.acquire()
        try:
            comdata = ser.readline(4)
            app.text.delete("0.0", tk.END)
            app.text.insert("0.0", comdata)
        finally:
            lock.release()

app.master.geometry("400x400")
app.master.title("sample")

t1 = Thread(target = COMread)
t2 = Thread(target = Write)
t1.daemon = True
t2.daemon = True
t1.start()
t2.start()

app.mainloop()

