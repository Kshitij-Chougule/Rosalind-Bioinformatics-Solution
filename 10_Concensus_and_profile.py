all_lines=[]
def seperation(all_lines):
    ID=[]
    sequences=[]
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
    return sequences
#def counting(bases):
A=[]
T=[]
G=[]
C=[]   
with open("sequence1.txt","r") as file:
    all_lines=file.readlines()
    lines=seperation(all_lines)
    bases=[list(sequence) for sequence in lines]
    for j in range(0,len(bases[0])):
        count_A=0
        count_T=0
        count_G=0
        count_C=0
        for i in range(0,len(bases)):
            for _ in bases[i][j]:
                if _ == 'A':
                    count_A+=1
                elif _ == 'T':
                    count_T+=1
                elif _ == 'G':
                    count_G+=1
                elif _ == 'C':
                    count_C+=1
        A.append(count_A)
        T.append(count_T)
        G.append(count_G)
        C.append(count_C)
    for i in range(0,len(A)):
        seq=max(A[i],T[i],G[i],C[i])
        if A[i]==seq:
            print("A",end="")
        elif T[i]==seq:
            print("T",end="")
        elif G[i]==seq:
            print("G",end="")
        elif C[i]==seq:
            print("C",end="")
    print()
    print("A:",end=" ")
    print(*A)
    print("C:",end=" ")
    print(*C)
    print("G:",end=" ")
    print(*G)
    print("T:",end=" ")
    print(*T)           