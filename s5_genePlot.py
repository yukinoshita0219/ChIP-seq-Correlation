#!/usr/bin/python3
# encoding=utf-8

from config import *
from table import readcols
import matplotlib.pyplot as plt
import numpy as np

def plot(axes, x, y, **kwargs):
    x = np.array(x)
    xl = len(x)
    yr = np.array(y).reshape(int(len(y)/xl), xl)
    ym = yr.mean(0)
    axes.plot(x, ym, **kwargs)
    parts = axes.violinplot(yr, x, showextrema=False, widths=100)
    for pc in parts['bodies']:
        pc.set_facecolor(kwargs['color'])

def readData(samples):
    col = readcols(path + samples + '_geneMean.txt')
    center = [int(i)+100 for i in col[1][:15]]
    value1 = [float(i) for i in col[3]]
    value2 = [float(i) for i in col[4]]
    return (center, value1, value2)

x, y1, y2 = readData('_'.join(samples))
fig, ax = plt.subplots(1, 1, True)
ax.set_title('Gene-nearby Coherence between RCM-1 & CBF-1')
ax.set_xlabel('Relative Position to Transcription Start')
ax.set_xlim(-2000, 1000)
xticks = [i-100 for i in x]
xticks.append(1000)
ax.set_xticks(xticks)
ax.set_ylabel('200bp Mean Signal')
ax.set_ylim(0, 30)
plot(ax, x, y1, color='red', label='RCM-1')
plot(ax, x, y2, color='blue', label='CBF-1')
ax.legend()
plt.show()
