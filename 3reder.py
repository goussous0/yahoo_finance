import os
import datetime as dt
import datetime
import matplotlib.dates as mdates
import csv
from clint.textui import puts,colored,indent
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.transforms as mtransforms
import numpy as np






tmp_lst = []





def intro(file):
    dates = []
    x = []
    k = []
    g = []
    y = []
    plt.rcParams['axes.facecolor'] = 'black'

    symbol = file[:len(file) - 4]




    with indent(12):
        puts(colored.yellow(symbol))
    with open(file , mode='r') as file_csv:
        lines= file_csv.readlines()
        default = 5
        for i, line in enumerate(lines):
            if i == 0:
                pass
            elif i >= len(lines)-default:
                line = str(line).replace(",", "  ")
                line = (line.split())
                tmp_lsst = []
                for j in range (5):
                    tmp_lsst.append(line[j])

                    tmp_lst.append(tmp_lsst)
                puts(colored.cyan(line[0] + "               " + str(line[1])))
                dates.append(line[0])
                y.append(line[1])
                puts(colored.blue(line[1]))
                k.append(line[2])
                puts(colored.green(line[2]))
                g.append(line[3])
                puts(colored.red(line[3]))

                default += 1


    x = [datetime.datetime.strptime(d, "%Y-%m-%d").date() for d in dates]


    # print (x)
    plt.matplotlib.pyplot.title(symbol)
    plt.plot(x, k, color='green')
    plt.plot(x, y, color='yellow')
    plt.plot(x, g, color='red')
    plt.show()



    # print (x)    print (tmp_lst)

if __name__ == "__main__":
    puts(colored.red("#################################################################################"))
    file = str(input("Please enter a file name : \n"))
    intro(file=file)