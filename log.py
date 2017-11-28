import serial 

ser = serial.Serial("COM5", baudrate=115200)

while True:
    logfile = open("c:\\files\\project_master\\log.txt", "a")
    received = ser.readline(4)
    strdata = str(received)
    logfile.writelines(strdata + "\n")
    logfile.close()    