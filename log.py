import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

i = 0
xar = []
yar = []
X = []
Y = []
database = "c:\\files\\project_master\\log.csv"

with open(database) as db:
    ejectdata = csv.reader(db)
    header = next(ejectdata)
    for row in ejectdata:
        try:
            if i % 2 == 0:
                yar.append(row[0])
                xar.append(row[1])
            else:
                Y.append(row[0])
                X.append(row[1])
            i = i + 1
        except IndexError:
            break

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    ax1.clear()
    #ax2.clear()
    ax1.plot(xar,yar)
    ax1.plot(X, Y, c ='red')
ani = animation.FuncAnimation(fig, animate, interval=30)

plt.show()