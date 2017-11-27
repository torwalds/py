import serial 

ser = serial.Serial("/dev/ttyAMA0", baudrate=115200)
logfile = open("log.txt", "w")

while True:
    received = ser.read(4)
    strdata = str(received)
    logfile.write(strdata + "\n")

logfile.close()    