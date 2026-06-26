#To find GC content of DNA string tried to code using basic python functions
#First defined a GC content calculator
def GC_content_of_seq(x):
    GC_content=0
    bases=list(x)
    for base in bases:
        if base=='G' or base=='C':
            GC_content+=1
    return float((GC_content/len(x))*100)
#Made list to store ID, sequence and GC_content for simplicity
ID=[]
sequences=[]
GC_content=[]
with open("sequence.txt","r") as file:
    all_lines=file.readlines()
    sequence=''
    for line in all_lines:
#Storing all ID lines(Identified them using '>')
        if line.startswith(">"):
            ID.append((line.strip()).strip(">"))
#Use length of list to know when to append(So that ID and its corrosponding sequence gets same index)
        elif len(ID)>len(sequences):
#This if block can successfuly append all sequences except the last one
            if (len(ID)-1)>len(sequences):
                sequences.append(sequence)
                sequence=''
            sequence+=line.strip()
#Since the last sequence cannot be appended by the previous if block
    sequences.append(sequence)
#Calculating GC content of all sequences and appending it
for s in sequences:
    GC_content.append(GC_content_of_seq(s))
answer=max(GC_content)
#printing final answer
print(ID[GC_content.index(answer)])
print(f"{answer:.6f}")