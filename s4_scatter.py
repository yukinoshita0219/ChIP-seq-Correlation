#!/usr/bin/python3
# encoding=utf-8

from config import *
import matplotlib.pyplot as plt
from scipy.stats import linregress
from table import *
import numpy as np

def draw(x, y=None):
    x, y = np.array(x), np.array(y)
    slope, intercept, rvalue, pvalue, stderr = linregress(x, y)
    fig, axs = plt.subplots(1, 2)
    axs[1].axis((1e-3, 1e3, 1e-3, 1e3))
    axs[1].set_xscale('log')
    axs[1].set_yscale('log')
    
    for ax in axs:
        ax.set_xlabel('RCM-1 1000bp Mean Signal')
        ax.set_ylabel('CBF-1 1000bp Mean Signal')
        ax.scatter(x, y, 1, marker='.')

    axs[0].set_title('Correlation between RCM-1 & CBF-1 (linear scale)')
    axs[0].text(100, 300, 'n = {}\nr = {}\n'.format(len(x), '%.4f' %float(rvalue)))
    axs[1].set_title('Correlation between RCM-1 & CBF-1 (log scale)')
    axs[1].text(0.1, 100, 'n = {}\nr = {}\n'.format(len(x), '%.4f' %float(rvalue)))

    plt.show()

def readvalue(samples, path=''):
    values = []
    for sam in samples:
        filename = path + sam + '_mean.txt'
        values.append(list(map(float, readcols(filename)[3])))
    return tuple(values)

def delzero(*inputs):
    i = 0
    n = len(inputs[0])
    while i < n:
        findzero = False
        for data in inputs:
            if data[i] == 0:
                findzero = True
        if findzero:
            for data in inputs:
                data.pop(i)
            i -= 1
            n -= 1
        i += 1
    return tuple(inputs)

x, y = readvalue(samples, dataPath)
draw(x, y)
