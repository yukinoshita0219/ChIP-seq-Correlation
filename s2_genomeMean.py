#!/usr/bin/python3
# encoding=utf-8

from config import *
from table import *

def wigmean(sample, size, path=''):
    with open(path + sample + '_mean.txt', 'w') as output:
        col = readcols(path + sample + '_filled.txt')
        start, mysum, chrom = 0, 0, col[0][0]
        end = start + size
        for i in range(len(col[0])):
            if chrom == col[0][i]:
                lower, upper, value = int(col[1][i]), int(col[2][i]), float(col[3][i])
                if upper < end:
                    mysum += (upper - lower) * value
                else:
                    mysum += (end - lower) * value
                    myave = '%.4f' %(mysum / size)
                    output.write('{}\t{}\t{}\t{}\n'.format(chrom, start, end, myave))
                    while (end + size) <= upper:
                        start, end = end, end + size
                        output.write('{}\t{}\t{}\t{}\n'.format(chrom, start, end, '%.4f' %value))
                    mysum = (upper - end) * value
                    start, end = end, end + size
            else:
                end = int(col[2][i-1])
                if end != start:
                    myave = '%.4f' %(mysum / (end - start))
                    output.write('{}\t{}\t{}\t{}\n'.format(chrom, start, end, myave))
                chrom, start, end, mysum = col[0][i], 0, size, 0
                i -= 1
            i += 1
        myave = '%.4f' %(mysum / (int(col[2][-1]) - start))
        output.write('{}\t{}\t{}\t{}\n'.format(chrom, start, col[2][-1], myave)) 

for sam in samples:
    wigmean(sam, size, path)
