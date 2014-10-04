print "Hello test"

dna_string = raw_input()

print dna_string
counting = [0,0,0,0]

for nucleotide in dna_string:
    if (nucleotide == 'A'):
        counting[0] += 1
    elif (nucleotide == 'T'):
        counting[1] += 1
    elif (nucleotide == 'C'):
        counting[2] += 1 
    elif (nucleotide == 'G'):
        counting[3] += 1

print "{} {} {} {}".format(counting[0], counting[2], counting[3], counting[1])
