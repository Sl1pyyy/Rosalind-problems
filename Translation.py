from INPUTDATA import prot_rna, RNA_to_PROT

def translation (prot_rna, init_position = 0):
    """ Translate mRNA to Protein sequence """
    return ''.join(RNA_to_PROT[prot_rna[pos:pos + 3]] for pos in range(init_position, len(prot_rna) - 2 , 3))

if __name__ == '__main__':
    print(translation(prot_rna))