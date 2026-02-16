from INPUTDATA import gc_cont

def gc_calc(seq):

    return f'{seq.count('G')+seq.count('C') / len(seq) * 100:.0f}%'

if __name__ == '__main__':
    print(gc_calc(gc_cont))