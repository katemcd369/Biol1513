#!/usr/bin/env python3

#import modules
import re
import csv
import argparse
from Bio import SeqIO
from collections import defaultdict


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


def codon2aa(codon):
    codon_dict = {'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'TAA':'O', 'TAC':'Y', 'TAG':'O', 'TAT':'Y', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TGA':'O', 'TGC':'C', 'TGG':'W', 'TGT':'C', 'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F'}
    return(codon_dict.get(codon, '-'))


def parse_gff(genome):
    #open and parse the gff file, and define the list
    with open(args.gff, 'r') as gff_file:
        reader = csv.reader(gff_file, delimiter= '\t')
        for line in reader:
            if not line:
                continue
            else:
                organism = line[0].replace(' ', '_')
                start = (int(line[3]) - 1)
                stop = int(line[4])
                strand = line[6]
                feature_type = line[2]
                attributes = line[8]

                #test to see if gene is CDS feature
                if (feature_type == 'CDS'):
                    string = attributes.split(' ')
                    name = string[1]

                    #extract the gene name using regex
                    match = re.search('Gene\s+(\S+)\s+', attributes)
                    gene_name = (match.group(1))

                    #extract sequence region for gene
                    sequence = genome[start:stop]
                    #feature_GC = gc(seq)
                    #print gene name and GC content
                    #print(parse[1] + " GC content = " + str('{0:2f}'.format(feature_GC)))

                    #reverse complement sequence if necessary, stor as reverse
                    if strand == '-':
                        reverse = sequence.reverse_complement()

                    #extract the exon number with regex and print in fasta format if applicable
                    #if not match, default is 1
                    match2 = re.search("exon\s(\d?)", attributes)

                    #make cds dictionary. key = gene name, value = other dict (key = exon number, value = exon sequence)
                    cds = defaultdict(dict)

                    #use regex to extract multiple exons if applicable
                    if match2:
                        exon_number = (match2.group(1))

                        #if feature is neg use complement strand
                        if strand =='-':
                            cds = {gene_name : {exon_number : reverse}}

                        #if feature is pos, use original
                        else:
                            cds = {gene_name : {exon_number : sequence}}

                        #print ('>' = str(organism) + '_' + str(gene_name) + '_' + 'exon_' + str(exon_number))
                        #print(sequence)

                    #if there is only one exon exon, use 1 as default exon dictionary key in hierarchy
                    else:
                        exon_number = 1
                        #do the same for positive and negative as before
                        if strand == '-':
                            cds = {gene_name : {exon_number : reverse}}

                        #if feature is pos, use original
                        else:
                            cds = {gene_name : {exon_number : sequence}}

                    for gene, seq in cds.items():
                        print('>' + str(organism) + '_' + str(gene_name))
                        
                        for ex in seq:
                            print(seq[ex])
                    

                    
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

# get the command-line arguments before calling main()
args = get_args()

#exicute program by calling main
if __name__ == "__main__":
    main()