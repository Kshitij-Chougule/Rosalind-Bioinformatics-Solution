all_lines = []
ID = []
sequences = []
common_substrings=[]
#To separate the lines and organizing in IDs and sequences
def seperation(all_lines):
    sequence = ''
    for line in all_lines:
        if line.startswith(">"):
            ID.append((line.strip()).strip(">"))
        elif len(ID) > len(sequences):
            if (len(ID) - 1) > len(sequences):
                sequences.append(sequence)
                sequence = ''
            sequence += line.strip()
    sequences.append(sequence)
    return sequences
#To open and read lines
with open("sequence3.txt","r") as file:
    all_lines=file.readlines()
    seperation(all_lines)
    sequences.sort(key=len)
#Using the first sequence from the sequence list as a reference to find shared motif
    se=sequences[0]
    for i in range(1,len(se)+1):
        for start in range(len(se)-i+1):
            score=0
            seq=se[start:i+start]
            for s in sequences:
#Using score as a parameter to measure how common a sequence is in the list
                if seq in s:
                    score+=1
#If not common the sequence will not be considered
                else:
                    break
# If common then put in list common_substrings
            if score==len(sequences):
                common_substrings.append(seq)
#Using num list to help find the longest substring
    num=[]
    for substrings in common_substrings:
        num.append(len(substrings))
    longest_substring=common_substrings[num.index(max(num))]
    print(longest_substring)