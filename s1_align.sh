#!/bin/sh

bowtie2-build ~/genome/NC10/Sequences/WholeGenomeFasta/genome.fa ~/genome/NC10/Sequences/Bowtie2Index/genome

mkdir histogram

for input in  'PAD1' 'PAB1' 'IAB1'
do 

mkdir $input

bowtie2 -p 8 -x ~/genome/NC10/Sequences/Bowtie2Index/genome -1 clean_data/$input\_1.clean.fq.gz -2 clean_data/$input\_2.clean.fq.gz -S $input/$input.sam 2>> $input/stats.txt
 
cd $input

samtools view -bS $input.sam > $input.bam
samtools sort -n $input.bam > $input\_sorted.bam
bedtools bamtobed -i $input\_sorted.bam -bedpe > sorted.bed

rm $input.sam

cd ..

perl filter_bed.pl $input

rm $input/sorted.bed
 
export File_name=$input

perl cal_ratio.pl

cd $input

source="ratio.txt"
ratio=$(cat $source)
echo $ratio

cd ..

sort -k1,1 -k2,2n $input/fragments.bed > $input/sorted.bed
bedtools genomecov -i $input/sorted.bed -scale $ratio -bg -g ~/genome/NC10/Genes/NC10.chrom > histogram/$input.wig

cd histogram
mkdir tdf

igvtools toTDF $input.wig tdf/$input.tdf nc10

cd ..

done
