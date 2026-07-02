all_lines = []
ID = []
sequences = []
parts = []

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
    return sequences, ID

# Read the file
with open("sequence2.txt", "r") as file:
    all_lines = file.readlines()
    sequences, ID = seperation(all_lines)
    
    # Extract prefixes and suffixes of length 3
    for se in sequences:
        part1 = se[0:3]   # Prefix of length 3
        part2 = se[-3:]   # Corrected: Suffix of length 3
        parts.append([part1, part2])
        
    # Check for directed overlaps (Suffix of i matching Prefix of j)
    for i in range(0, len(parts)):
        suffix_i = parts[i][1] # Suffix of sequence i
        
        for j in range(0, len(parts)):
            if i == j: 
                continue
                
            prefix_j = parts[j][0] # Prefix of sequence j
            
            # If suffix matches prefix, it forms a directed edge: ID[i] -> ID[j]
            if suffix_i == prefix_j:
                print(ID[i], ID[j])
