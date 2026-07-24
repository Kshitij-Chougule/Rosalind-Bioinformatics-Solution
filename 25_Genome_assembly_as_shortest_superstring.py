# Defining a function to extract DNA sequences from the given file
def extract_DNA_sequences(all_lines):
    ID=[]
    sequences=[]
    sequence=''
    for line in all_lines:
        if line.startswith(">"):
            ID.append(line)
        if len(ID)-1==len(sequences) and not line.startswith(">"):
            sequence+=line.strip()
        if len(ID)-1>len(sequences):
            sequences.append(sequence)
            sequence=''
    sequences.append(sequence)
    return sequences
# Defining a function to assemble the superstring
def assemble(strings):
    strings = strings[:]
# Removing the first string from the strings list
    superstring = strings.pop(0)
# Using approach (Adding string to super string and then removing it from the strings list)
    while strings:
        merged = False
# i is the index and s is the string
        for i, s in enumerate(strings):
            n = min(len(superstring), len(s))
# First for loop to check that if tail of superstring is equal to head of s
            for l in range(n, n // 2, -1):
                if superstring[-l:] == s[:l]:
                    superstring += s[l:]
                    strings.pop(i)
                    merged = True
                    break
            if merged:
                break
# If the previous condition is not satisfied checked for tail of s and head of superstring
            for l in range(n, n // 2, -1):
                if s[-l:] == superstring[:l]:
                    superstring = s + superstring[l:]
                    strings.pop(i)
                    merged = True
                    break
            if merged:
                break
# If both the conditions did not match asked to raise an error
        if not merged:
            raise ValueError("No overlapping read found")

    return superstring
with open("sequence6.txt","r") as file:
    lines=file.readlines()
    super_string=assemble(extract_DNA_sequences(lines))
    print(super_string)