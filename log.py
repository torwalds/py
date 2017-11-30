import serial 
import os
import sys

ser = serial.Serial("COM5", baudrate=115200)
global out

while True:
    logfile = open("c:\\files\\project_master\\log.txt", "a")
    received = ser.readline(4)
    out = received
    strdata = str(received)
    logfile.writelines(strdata + "\n")
    logfile.close()    