# Using the logic of recursion
def enumerate_kmers(alphabet,n):
    if n==0:
        return ['']
    smaller=enumerate_kmers(alphabet,n-1)
    result=[]
    for letter in alphabet:
        for suffix in smaller:
            result.append(letter+suffix)
    return result
alphabet=['A','B','C','D','E','F','G','H']
kmers=enumerate_kmers(alphabet,3)
for kmer in kmers:
    print(kmer)