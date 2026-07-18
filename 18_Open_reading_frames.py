DNA_sequence="AATGACACTTTTGCTGGTAGAGACGCTGCTGGTTACCTTGTAGACGCTCACCGCCCGAGTTTCTCAGCAACCCCGGACCGTCGTCGCTTTAGAGTGCGAAGGTGATGCCCGTCAATTCAATCGAAAAGACGCACTAGCGAAGCTCAAGCTGTGCCTCCAGTATCCGAATTCAAATCATTGTCTCATTCAGGAGATACCCCAACACTGCACGTTACTAGACTTTTCATAATTATCTTTGAGCCATAATACGATATATTGTGAGACTTACAAAACACTACTACAGAGGTGCATCGTCCCATGACATGTTCGACGAAATACACTTGCTACGTATGGTCCAGCTCGGCGTCGATGCCACTTTGAGCAAATCAGCAACCCCGGCGTCCGTATGCGGGACCTAACTTAGGGTACCGCACCACACTAAATGGATTGAAATGTCGGTGTGCTCGTCGTGCTAGCTAGCACGACGAGCACACCGACATAATTGGCTGTTCGGGATCCCCGTTCCCCGTGTTGGTGGTTGTAGGCGACTTGTACCCTTGAAATTATATTAGCTGGACTGGTCCAAGGTTCTTTCGGTGAGTGCGGAAGGGTTATCAGCTAAATAAGAAACATACGCGCAAACGAACCTTACCTGGAAGAGGCAAAATTACAGTCCTTATTTCAGTGTAAGCCGCGCAATAAGCGTCTTGGAGTTGATTCCAAAAGATGCCGCATGGGCGTTCCGCCGTTCGAACCCTTCGCAGTCCCCTTTCGGCCTTCAAGTAGTTCTTGGGTTCATTGCACAAATGGAGGTTGCAGTGACAGCGCAGAATACTTTTGCTCTCGTGGTGATCGTCTCCGTAGGGTGTCGTGAGGACACCGCTTCTCTAAGACCTTAGAACATATTATCTGCATCTTCTCCCCCCGCAAG"
#Creating a complementary strand
def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(complement[base] for base in reversed(dna))
#Function to find amino acid of a codon
def translate_codon(codon):
    codon_table = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M','ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T','AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R','CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L','CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P','CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q','CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R','GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A','GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G','TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L','TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGA':'_','TGT':'C','TGC':'C','TGG':'W'}
    return codon_table.get(codon,"")
#Function to make a sequence
def sequence_creation(dna):
    sequence=[]
    for i in range(len(dna)):
        line=''
        if dna[i:i+3]=="ATG":
            for j in range(i,len(dna),3):
                if dna[j:j+3] in ["TAA","TAG","TGA"]:
                   line=dna[i:j+3]
                   sequence.append(line)
                   break
    return sequence
#Function to take sequence list and translate them one by one
def protein_creation(dna):
    proteins=[]
    sequences=sequence_creation(dna)
    for sequence in sequences:
        codons=[]
        proteinseq=''
        for i in range(0,len(sequence),3):
            codons.append(sequence[i:i+3])
        for codon in codons:
            proteinseq+=translate_codon(codon)
#Used strip function since stop codon is denoted by '_'
        proteins.append(proteinseq.strip('_'))
    return proteins
reverse=reverse_complement(DNA_sequence)
#Done so that the protein sequences do not overlap
protein_set=set(protein_creation(DNA_sequence)+protein_creation(reverse))
#Done to format output
for protein in protein_set:
    print(protein)