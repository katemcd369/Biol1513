#!/usr/bin/env python3

#import modules
import csv
import argparse

#create and argument parse object
parser = argparse.ArgumentParser(description = 'This script will take a .gff file, pull out the gene names from the list, and store them in a alphabatized list. Then it will take that list and use it to pull out the gene sequences from a fasta file and calculate the GC content.')

#add positional arguments for the gff and fasta files to be used
parser.add_argument('gff', help= 'The name of the .gff file you wish to use', type=str)
parser.add_argument('fasta', help= "The name of the fasta file you wish to use", type=str)

#parse the arguments
args = parser.parse_args()
#define files
gff_file = 'watermelon.gff'
fasta_file = 'watermelon.fsa'
#open and parse the gff file, and define the list
with open(args.gff, 'r') as gff:
    gene_names = []
    reader = csv.reader(gff, delimiter= '\t')
    for line in reader:
        if not line:
            continue
        else:
            #separate out the repeated or similar to genes
            if (line[2] != 'misc_feature' and line[2] != 'repeat_region'):
               #pull out gene name and add it to the list
                parse = line[8].split(' ')
                gene_names.append(parse[1])

#print the gene games in alphabetical order
for gene in sorted(gene_names):
    print(gene)

gff.close

#open and close the fasta file
with open(args.fasta, 'r')as fasta:
    
    fasta.close