#!/usr/bin/env python3

infile = 'watermelon.gff'

with open(infile, 'r') as melon:
    gene = []
    for line in melon:
        line = line.rstrip('\n')
        fields = line.split('\t')
        if (fields[2] != 'misc_feature' and fields[2] != 'repeat_region'):
            parse = fields[8].split(' ')
            gene.append(parse[1])

    gene.sort()
    print(gene)
