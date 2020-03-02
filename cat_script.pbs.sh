#!/bin/bash

#PBS -N Blast
#PBS -q tiny12core
#PBS -j oe
#PBS -m abe
#PBS -M katemcd@uark.edu
#PBS -o cat.txt
#PBS -l nodes=1:ppn=12
#PBS -l walltime=00:00:10:00

module load python/3.6.0-andaconda

cat_seqs.py