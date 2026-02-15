from INPUTDNA import DNA_reverse, rev_data

def reverse_dna(seq):
    return ''.join([DNA_reverse[nuc] for nuc in seq])[::-1]

if '__main__' == __name__:
    print(f" 3' {rev_data} 5' ")
    print(f"    {''.join(['|' for s in range(len(rev_data))])} ")
    print(f" 5' {reverse_dna(rev_data)} 5' ")