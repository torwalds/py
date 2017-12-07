from tkinter import *
from tkinter import font
import os
import glob
import time
import threading
import queue as qe
from queue import Empty
import serial
import csv

ser = serial.Serial("COM5", baudrate=115200)
logfile = open("c:\\files\\project_master\\log.csv", "a")
i = 0

def update_temp(queue):
    global i
    while True:
        i = i + 0.005
        tempread_1 = ser.readline(4)
        tempread_2 = ser.readline(4)
        strdata_1 = str(tempread_1, 'utf-8')
        strdata_2 = str(tempread_2, 'utf-8')
        logfile.writelines(strdata_1 + "," + str("%.3f" % i) +"," + "\n")
        logfile.writelines(strdata_2 + "," + str("%.3f" % i) +"," + "\n")
        queue.put(tempread_1)
        queue.put(tempread_2)
        #time.sleep(0.001)

class Gui(object):
    def __init__(self, queue):
        self.queue = queue
        #Make the window
        self.root = Tk() 
        self.root.overrideredirect(1)
        self.root.wm_title("Home Management System")
        #self.root.minsize(400, 400)
        self.root.geometry('%dx%d+%d+%d' % (400, 400, 500, 500))

        self.equipTemp = StringVar()        
        self.equipTemp1 = StringVar() 
        
        labelpass = Label(self.root, font=("Impact", 20), foreground = "black", text="Value first: ")
        labelpass.place(x=0,y=0)

        Label2=Label(self.root, textvariable=self.equipTemp, font=("Impact", 20), foreground = "red", justify=RIGHT)
        Label2.place(x=180, y=0)

        labelpass2 = Label(self.root, font=("Impact", 20), foreground = "black", text="Value second: ")
        labelpass2.place(x=0,y=50)

        Label3=Label(self.root, textvariable=self.equipTemp1, font=("Impact", 20), foreground = "red", justify=RIGHT)
        Label3.place(x=180, y=50)

        bQuit = Button(self.root, text="Quit", command=self.root.quit)
        bQuit.place(x = 0, y = 100)

        self.root.after(300, self.read_queue)

    def read_queue(self):
        try:
            temp1 = self.queue.get_nowait()
            temp2 = self.queue.get_nowait()
            self.equipTemp.set(temp1)
            self.equipTemp1.set(temp2)
        except qe.Empty:
            pass

        self.root.after(300, self.read_queue)

if __name__ == "__main__":
    queue = qe.LifoQueue()
    t = threading.Thread(target=update_temp, args=(queue,))
    t.daemon = True
    t.start()
    # Build GUI object
    gui = Gui(queue)
    # Start mainloop
    
    gui.root.mainloop()
    logfile.close()  