#!/usr/bin/python3
# encoding=utf-8

from config import *
from table import *

def wigfill(sample, path=''):
    with open(path + sample + '.wig', 'r') as fin:
        with open(path + sample + '_filled.txt', 'w') as fout:
            col = readcols(path + 'NC10.chrom')
            chromsize = dict(zip(col[0], col[1]))
            lines = fin.readlines()
            line = lines[0].strip().split('\t')
            chrom = line[0]
            if line[1] != '0':
                fout.write('{}\t{}\t{}\t{}\n'.format(chrom, 0, line[1], 0.0))
            fout.write(lines[0])
            for i in range(1, len(lines)):
                lineb, line = line, lines[i].strip().split('\t')
                if chrom != line[0]:
                    if chromsize[chrom] > lineb[2]:
                        fout.write('{}\t{}\t{}\t{}\n'.format(chrom, lineb[2], chromsize[chrom], 0.0))
                    chrom = line[0]
                    if line[1] != 0:
                        fout.write('{}\t{}\t{}\t{}\n'.format(chrom, 0, line[1], 0.0))
                else:
                    if line[1] != lineb[2]:
                        fout.write('{}\t{}\t{}\t{}\n'.format(chrom, lineb[2], line[1], 0.0))
                fout.write(lines[i])
            if chromsize[chrom] > line[2]:
                fout.write('{}\t{}\t{}\t{}\n'.format(chrom, line[2], chromsize[chrom], 0.0))

for sam in samples:
    wigfill(sam, dataPath)
