Nucleotides = ['A','T','G','C']

DNA_reverse = {'A':'T','T':'A','G':'C','C':'G'}

RNA_to_PROT = {
'UUU': 'F', 'CUU': 'L',  'AUU':'I',     'GUU': 'V',
'UUC': 'F', 'CUC': 'L',  'AUC': 'I',    'GUC': 'V',
'UUA': 'L', 'CUA': 'L',  'AUA': 'I',    'GUA': 'V',
'UUG': 'L', 'CUG': 'L',  'AUG': 'M',    'GUG': 'V',
'UCU': 'S', 'CCU': 'P',  'ACU': 'T',    'GCU': 'A',
'UCC': 'S', 'CCC': 'P',  'ACC': 'T',    'GCC': 'A',
'UCA': 'S', 'CCA': 'P',  'ACA': 'T',    'GCA': 'A',
'UCG': 'S', 'CCG': 'P',  'ACG': 'T',    'GCG': 'A',
'UAU': 'Y', 'CAU': 'H',  'AAU': 'N',    'GAU': 'D',
'UAC': 'Y', 'CAC': 'H',  'AAC': 'N',    'GAC': 'D',
'UAA': '_', 'CAA': 'Q',  'AAA': 'K',    'GAA': 'E',
'UAG': '_', 'CAG': 'Q',  'AAG': 'K',    'GAG': 'E',
'UGU': 'C', 'CGU': 'R',  'AGU': 'S',    'GGU': 'G',
'UGC': 'C', 'CGC': 'R',  'AGC': 'S',    'GGC': 'G',
'UGA': '_', 'CGA': 'R',  'AGA': 'R',    'GGA': 'G',
'UGG': 'W', 'CGG': 'R',  'AGG': 'R',    'GGG': 'G'
}

data = 'CCCTAAGGTGCTTATGTTAGGGCGACGCCGGCCCTCTCCGGACAAA'

raw_dna = 'TGTATCCGGTCGACTCTTTCTCATGCAGCCGACAGCCAGTTAA'

rev_data = 'TTGTCGCCGAATTAATTCCCTCCCTCGTACACATATCAAAAT'

prot_rna = 'AUGGCCUUAUGUAAAUGA'

gc_cont = 'AUGGCCUUAUGUAAAUGA'