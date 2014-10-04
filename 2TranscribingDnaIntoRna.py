dna_string = raw_input()
rna_string = []

for nucleotide in dna_string:
    if (nucleotide == 'T'):
        rna_string.append('U')
    else:
        rna_string.append(nucleotide)

print ''.join(rna_string)
