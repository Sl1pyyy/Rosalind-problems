from INPUTDATA import Nucleotides

def vernucstr(dnaseq):
    """ Functiom, that verifies if the DNA/RNA string contains actual nucleotides"""
    tmpseq =  dnaseq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return None
    return tmpseq

