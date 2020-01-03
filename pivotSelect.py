import csv, random, heapq
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

def getDataSet(data_path, d, number, sample='random'):
    data = []
    with open(data_path)as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            data.append(row)
    if sample == 'random':
        index = [random.randint(0, 1000) for i in range(number)]
    elif sample == 'fft':
        point_dist = [sum([distance(ele[1:2], da[1:2]) for ele in data]) for da in data]
        index = map(point_dist.index, heapq.nlargest(number, point_dist))
    data_select = [[data[i][j] for j in range(1, d + 1)] for i in index]
    return np.array(data_select)

def distance(x, y):
    if len(x) == len(y):
        return sqrt(sum([(float(x[i]) - float(y[i])) ** 2 for i in range(len(x))]))


def evaluate(setE, d, pivot):
    # 只有一个支撑点
    if len(pivot) <= 1:
            dist = [distance(pivot[0], ele) for ele in setE]
            return np.var(np.array(dist))
    # 有两个及以上的支撑点
    else:
        # 从度量空间映射到支撑点空间
        setE_pivot = np.array([[distance(pivot[i], ele) for i in range(len(pivot))]for ele in setE])
        # plt.scatter([ele[0] for ele in setE_pivot],[ele[1] for ele in setE_pivot])
        # plt.show()
        # 计算两两数据之间的累加和，再求平均
        setE_dist = [[max(abs(setE_pivot[i]-setE_pivot[j]))for j in range(i)] for i in range(len(setE_pivot))]
        return sum([sum(ele) for ele in setE_dist])/(len(setE_dist)**2)


def pivotSelection(data, d, numPivot):
    setC = getDataSet(data, d, 10, sample='fft')
    setE = getDataSet(data, d, 300, sample='random')
    Pivot = []
    for i in range(numPivot):
        bestValue = 0.0
        bestPoint = None
        for x in setC:
            if i == 0:
                prePivot = [x]
            else:
                prePivot = [Pivot[0], x]
            value = evaluate(setE, d, prePivot)
            if value > bestValue:
                bestValue = value
                bestPoint = x
        Pivot.append(bestPoint)
    return Pivot
