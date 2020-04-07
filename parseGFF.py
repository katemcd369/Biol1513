#!/usr/bin/env python

#import modules
import csv
import argparse
from Bio import SeqIO

#create and argument parse object
parser = argparse.ArgumentParser(description = 'This script will take a .gff file, pull out the gene names from the list, and store them in a alphabatized list. Then it will take that list and use it to pull out the gene sequences from a fasta file and calculate the GC content.')

#add positional arguments for the gff and fasta files to be used
parser.add_argument('gff', help= 'The name of the .gff file you wish to use', type=str)
parser.add_argument('fasta', help= "The name of the fasta file you wish to use", type=str)

#parse the arguments
args = parser.parse_args()

#read and parse the fasta file
genome = SeqIO.read(args.fasta, 'fasta')

#open and parse the gff file, and define the list
with open(args.gff, 'r') as gff:
    reader = csv.reader(gff, delimiter= '\t')
    for line in reader:
        if not line:
            continue
        else:
            #test to see if gene is CDS feature
            if (line[2] != 'CDS'):
               continue
            else:
                parse = line[8].split(' ')
                #pull out the start and stop position for the gene
                start = int(line[3])
                stop = (int(line[4]) + 1)
                #extract sequence region for gene
                seq = genome.seq[start:stop]
                #calculate GC content
                g_count = seq.count('G')
                c_count = seq.count('C')
                total = len(seq)
                gc_total = g_count + c_count
                content = float(gc_total) / total
                #print gene name and GC content
                print(parse[1] + " GC content = " + str('{0:2f}'.format(content)))

#close all files
gff.close()                