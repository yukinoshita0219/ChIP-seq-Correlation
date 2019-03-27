#!/usr/bin/python3
# encoding=utf-8

from config import *
from table import *

def genePos(filename):

    '''Get name, chromsome, and transcription start position of genes using refFlat.txt.

    Please use path of refFlat.txt as argument. Results will retern in 3 lists.'''
    cols = readcols(filename)
    gene = cols[0]
    chrom = cols[2]
    strand = cols[3]
    txStart = []
    for i in range(len(strand)):
        if strand[i] == '+':
            txStart.append(int(cols[4][i]))
        else:
            txStart.append(-int(cols[5][i]))
    return (gene, chrom, txStart)

def windowMean(chrIndex, winStart, winSize, data):
    for i in range(chrIndex, len(data[0])):
        if int(data[2][i]) > winStart:
            break
    shift = (int(data[2][i]) - winStart)
    if shift >= winSize:
        myave = float(data[3][i])
    else:
        mysum = shift * float(data[3][i])
        while shift < winSize:
            span = int(data[2][i]) - int(data[1][i])
            value = float(data[3][i])
            if shift + span >= winSize:
                mysum += (winSize - shift) * value
                myave = float('%.4f' %(mysum / winSize))
            else:
                mysum += span * value
            shift += span
            i += 1
    return myave

def indexChrom(data):
    chroms = readcols('NC10.chrom')[0]
    chrIndex = {}
    for chrom in chroms:
        chrIndex[chrom] = data[0].index(chrom)
    return chrIndex

genes, chroms, txStarts = genePos(path + 'refFlat.txt')
txStarts = [int(item) for item in txStarts]

dataset = []
indexset = []
for sam in samples:
    print('Reading {} data...'.format(sam), end='')
    data = readcols(path + sam + '_filled.txt')
    dataset.append(data)
    indexset.append(indexChrom(data))
    print('Done.')
        
with open(path + '_'.join(samples) + '_geneMean.txt', 'a') as outf:
    progress = genes.index(readcols(path + '_'.join(samples) + '_geneMean.txt')[0][-1]) + 1
    for i in range(progress, len(genes)):
        rpos = upstream
        while rpos < downstream:
            apos = txStarts[i] + rpos
            if apos < 0:
                apos = abs(apos) - window
            result = []
            for j in range(len(dataset)?!?jedi=0, ):?!? (chrIndex, winStart, *_*winSize*_*, data) ?!?jedi?!?
                result.append(windowMean(indexset[j][chroms[i]], apos, window, dataset[j]))
            result = '\t'.join([str(num) for num in result])
            outf.write('{}\t{}\t{}\t{}\n'.format(genes[i], rpos, rpos+window, result))
            rpos += window
        print('{} written.\n'.format(genes[i]))            
