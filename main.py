from tkinter import *
from tkinter import font
import os
import glob
import time
import threading
import queue as qe
from queue import Empty
import serial

ser = serial.Serial("COM5", baudrate=115200)
logfile = open("c:\\files\\project_master\\log.txt", "a")

def update_temp(queue):
    while True:

        tempread=ser.readline(4)
        strdata = str(tempread)
        logfile.writelines(strdata + "\n")
        queue.put(tempread)
        #time.sleep(0.01)

class Gui(object):
    def __init__(self, queue):
        self.queue = queue

        #Make the window
        self.root = Tk() 
        self.root.wm_title("Home Management System")
        self.root.minsize(400, 400)

        self.equipTemp = StringVar()        

        #Garage Temp Label
        labelpass = Label(self.root, font=("Impact", 20), foreground = "black", text="Current value: ")
        labelpass.place(x=0,y=0)
        Label2=Label(self.root, textvariable=self.equipTemp, font=("Impact", 20), foreground = "red", justify=RIGHT)
        Label2.place(x=180, y=0)

        self.root.after(300, self.read_queue)

    def read_queue(self):
        try:
            temp = self.queue.get_nowait()
            self.equipTemp.set(temp)
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