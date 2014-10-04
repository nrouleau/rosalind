dna_string = raw_input()
dna_complement = []

for nucleotide in reversed(dna_string):
    if (nucleotide == 'A'):
        dna_complement.append('T')
    elif (nucleotide == 'T'):
        dna_complement.append('A')
    elif (nucleotide == 'C'):
        dna_complement.append('G')
    elif (nucleotide == 'G'):
        dna_complement.append('C')

print ''.join(dna_complement)
