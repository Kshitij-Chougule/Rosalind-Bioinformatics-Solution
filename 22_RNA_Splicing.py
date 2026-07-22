# Codon Table
codon_table = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M','ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T','AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R','CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L','CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P','CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q','CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R','GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A','GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G','TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L','TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGA':'_','TGT':'C','TGC':'C','TGG':'W'}
# Separating DNA from the list
def DNA_with_introns(lines):
    ID=[]
    sequence_with_intron=''
    for line in lines:
        if line.startswith(">"):
            ID.append(line)
        if len(ID)<2 and not line.startswith(">"):
            sequence_with_intron+=line.strip()
        if len(ID)==2:
            return sequence_with_intron
# Taking Introns from given lines i.e. excluding the DNA part
def introns(lines):
    ID=[]
    introns=[]
    intron=''
    for line in lines:
        if line.startswith(">"):
            ID.append(line)
# For first case
        if len(introns)==0:
            if len(ID)==2 and not line.startswith(">"):
                intron+=line.strip()
            if len(ID)==3 and not line.startswith(">"):
# First intron added in list
                introns.append(intron)
                intron=''
# After the first intron is added
        if len(introns)>0:
            if len(ID)-2==len(introns) and not line.startswith(">"):
                intron+=line.strip()
            if len(ID)-2>len(introns):
                introns.append(intron)
                intron=''
# This is done for the last case since it cannot satify the previous if statement
    introns.append(intron)
    return introns
with open("sequence5.txt","r") as file:
    all_lines=file.readlines()
    DNA=DNA_with_introns(all_lines)
    m=introns(all_lines)
# For statements used to remove the introns from the DNA string
    for intron in m:
        for i in range(0,len(DNA)):
            if intron==DNA[i:i+len(intron)]:
                DNA=DNA.replace(DNA[i:i+len(intron)],"")
# Making codons of the DNA string without intron
    codons=[DNA[i:i+3] for i in range(0,len(DNA),3)]
    protein=''
    for codon in codons:
# Taking amino acid for codons
        protein+=codon_table.get(codon)
# Printing answer without the _(Value asigned for stop codon)
    print(protein.strip("_"))