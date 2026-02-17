from INPUTDATA import gc_cont

def gc_calc(seq):

    return f'{seq.count('G')+seq.count('C') / len(seq) * 100:.0f}%'

if __name__ == '__main__':
    print(gc_calc(gc_cont))

def readFile(filePath):
    """Reading a file and returning a list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]


def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round(
        ((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)


# Storing File contents in a list
FASTAFile = readFile("test_data/gc_content.txt")
# Dictionary for Labels + Data
FASTADict = {}
# String for holding the current label
FASTALabel = ""

# Converting FASTA/List file data into a dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

# Using Dictionary Comprehension to generate a new dictionary with GC content value
RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

# Looking for max value in values() of our new dictionary
MaxGCKey = max(RESULTDict, key=RESULTDict.get)

# Printing Rosalind formatted result
print(f'{MaxGCKey[1:]}\n{RESULTDict[MaxGCKey]}')