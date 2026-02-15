from DNAToolkit import *
from INPUTDATA import raw_dna

print(verdnastr(raw_dna))

#Define the function, which replaces T with U
def transcription(rep_rna):
    return rep_rna.replace('T', 'U')

if __name__ == '__main__':
    print(transcription(raw_dna))