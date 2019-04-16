#!/bin/bash

mkdir 'MACS2'

mkdir "MACS2/RCM1"
macs2 callpeak -t PAB1/PAB1_sorted.bam -c IAB1/IAB1_sorted.bam -f BAM -g 4.1e7 --broad --broad-cutoff 0.1 -n RCM1 --outdir MACS2/RCM1 -B --fix-bimodal

mkdir "MACS2/CBF1"
macs2 callpeak -t PAD1/PAD1_sorted.bam -c IAB1/IAB1_sorted.bam -f BAM -g 4.1e7 --broad --broad-cutoff 0.1 -n CBF1 --outdir MACS2/CBF1 -B --fix-bimodal
