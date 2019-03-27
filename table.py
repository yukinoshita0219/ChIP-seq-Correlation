#!/usr/bin/python3
# encoding=utf-8

def readcols(filename):
    col = []
    with open(filename, 'r') as t:
        lines = t.readlines()
        num = len(lines[0].strip().split('\t'))
        for i in range(num):
            col.append([])
        for line in lines:
            i = 0
            for data in line.strip().split('\t'):
                col[i].append(data)
                i += 1
    return col
