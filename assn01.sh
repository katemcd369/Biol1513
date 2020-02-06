#! bin/bash

#assn01-1

$ find /home -name *nad*

#assn01-2

$top 
# top - 15:55:49 up 17 min,  0 users,  load average: 0.52, 0.58, 0.59
# Tasks:   4 total,   1 running,   3 sleeping,   0 stopped,   0 zombie
# %Cpu(s):  0.7 us,  1.4 sy,  0.0 ni, 97.6 id,  0.0 wa,  0.3 hi,  0.0 si,  0.0 st
# KiB Mem :  8016248 total, 4122812 free, 3664084 used, 229352 buff/cache
# KiB Swap: 24117248 total, 24098552 free, 18696 used. 4218432 avail Mem 

#assn01-3
$cd watermelon_files | grep misc_feature watermelon.gff | sort -k7gr > IR_regions.gff

#assn01-4
$ echo non-IR; grep -cv IR IR_regions.gff; echo IR; grep -c IR IR_regions.gff  
# non-IR 34 IR 3

#assn01-5
# BamHI GGATCC EcoRI GAATTC

$ cd watermelon_nt; grep -vB1 GAATTC *.fasta| grep -B1 GGATCC *.fasta

#assn01-6
$ cd example_files; cat shaver_et_al.csv | head -n1000 | tail -n501 >shaver500_1000.csv

#assn01-7
$ column -t fruit.txt | sort -k2r,2 -k3,3 fruit.txt  
