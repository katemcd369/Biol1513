#! /usr/bin/env python3
#write a scripts in a text file file dna.txt calculate the nucleotide composition (%) for each base to print to the screen

#define variables
file = open('dna.txt', 'r')
dna = file.read().upper()
total = len(dna)
A_count = dna.count('A')
T_count = dna.count('T')
C_count = dna.count('C')
G_count = dna.count('G')
comp_a = 100 * (A_count / total)
comp_t = 100 * (T_count / total)
comp_c = 100 * (C_count / total)
comp_g = 100 * (G_count / total)
#printing out 
print('all bases:', str(total))
print('As: ' + '{:.5}'.format(str(comp_a)) + '%')
print('Ts: ' + '{:.5}'.format(str(comp_t)) + '%')
print('Cs: ' + '{:.5}'.format(str(comp_c)) + '%')
print('Gs: ' + '{:.5}'.format(str(comp_g)) + '%')

file.close()
