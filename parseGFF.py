#!/usr/bin/env python

#import modules
import csv
import argparse
from Bio import SeqIO


def get_args():
    #create and argument parse object
    parser = argparse.ArgumentParser(description = 'This script will take a .gff file, pull out the gene names from the list, and store them in a alphabatized list. Then it will take that list and use it to pull out the gene sequences from a fasta file and calculate the GC content.')

    #add positional arguments for the gff and fasta files to be used
    parser.add_argument('gff', help= 'The name of the .gff file you wish to use', type=str)
    parser.add_argument('fasta', help= "The name of the fasta file you wish to use", type=str)

    #parse the arguments
    return parser.parse_args()

def parse_fasta():
    #read and parse the fasta file
    return SeqIO.read(args.fasta, 'fasta')

def parse_gff(genome):
    #open and parse the gff file, and define the list
    with open(args.gff, 'r') as gff_file:
        reader = csv.reader(gff_file, delimiter= '\t')
        for line in reader:
            if not line:
                continue
            else:
                #test to see if gene is CDS feature
                if (line[2] == 'CDS'):
                    parse = line[8].split(' ')
                    #pull out the start and stop position for the gene
                    start = (int(line[3]) - 1)
                    stop = int(line[4])
                    #extract sequence region for gene
                    seq = genome[start:stop]
                    feature_GC = gc(seq)
                    #print gene name and GC content
                    print(parse[1] + " GC content = " + str('{0:2f}'.format(feature_GC)))
                    
def gc(sequence):
    #calculate GC content
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total = len(sequence)
    gc_total = g_count + c_count

    return (float(gc_total) / total)

def main():
    genome_sequence = parse_fasta()
    parse_gff(genome_sequence.seq)

#get the command line arguments before calling main
args = get_args()

#exicute program by calling main
if __name__ == "__main__":
    main()
              