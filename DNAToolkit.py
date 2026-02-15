from INPUTDATA import Nucleotides

#Functiom, that verifies if the DNA string contains actual nucleotides
def verdnastr(dnaseq):
    tmpseq =  dnaseq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return None
    return tmpseq

