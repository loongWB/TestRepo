
#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

filedir = "E:\Pycharm\Project\TestDemo\SrcData.txt"
#newFileDir = "E:\Pycharm\Project\TestDemo\NewData.txt"

volData = []
powerData = []

def esl_GetBatteryPower(voltage):

    BatteryPower = 0

    if voltage > 4.2:
        return 100
    elif voltage < 3.3:
        return 0
    else:
        if voltage >= 3.5:
            BatteryPower = - 322.03*voltage*voltage*voltage*voltage\
                           + 4519.5*voltage*voltage*voltage\
                           - 23553*voltage*voltage\
                           + 54085*voltage\
                           - 46211
        else:
            BatteryPower = 32.08*voltage*voltage\
                         - 189.7*voltage\
                         + 280.73

    if BatteryPower > 100:
        BatteryPower = 100
    return BatteryPower

def func(x,a,b,c,d):
    return a * x * x * x + b * x * x + c * x + d

def calc():
    fp = open(filedir,'r')
    print("filename:",fp.name)
    srcdata = fp.read().split()
    #srcdata = [1,2,3,4,5,6,7,8,9,10]
    for index in range(0,len(srcdata),2):
        if float(srcdata[index]) >= 3.5 and float(srcdata[index]) <= 4.1:
            volData.append(float(srcdata[index]))
            powerData.append(float(srcdata[index+1]))
    plt.scatter(volData[:],powerData[:],1,"red")
    a,b,c,d = optimize.curve_fit(func, volData, powerData)[0]
    print(a,b,c,d)
    print(esl_GetBatteryPower(3.51))
    x = np.arange(3.5, 4.12, 0.01)

    y1 = int(a)*x*x * x + int(b)*x * x +int(c) * x +d

    plt.plot(x, y1, "green")


    plt.title("test")

    plt.xlabel('x')

    plt.ylabel('y')
    plt.show()

    #print("Ready to Write...")

    print("Calculate Successfully!")
    fp.close()

if __name__ == '__main__':
    calc()