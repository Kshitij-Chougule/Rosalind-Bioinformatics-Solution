# To find N-glycosylation motif in the given proteins list
import requests, re

def fetch_protein(uniprot_id):
    #Taking URL of a given protein_id
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    resp = requests.get(url)
    #Raises an HTTP error if any
    resp.raise_for_status()
    lines = resp.text.splitlines()
    #Taken 1 to just take the amino acid sequence
    return "".join(lines[1:])

def location(uniprot_ids):
    motif = r"(?=(N[^P][ST][^P]))"
    ids, sequences = [], []
    for uniprot_id in uniprot_ids:
        #To just get the ID and not other letters that come after _
        clean_id = uniprot_id.split('_')[0]
        ids.append(uniprot_id)
        sequences.append(fetch_protein(clean_id))
    for uid, se in zip(ids, sequences):
        #To find location and added 1 to start counting from 1 instead of 0
        positions = [m.start() + 1 for m in re.finditer(motif, se)]
        if positions:
        # If the amino acid sequence has motif then
            print(uid)
            print(" ".join(map(str, positions)))

given_ids = []
# Done to format the given ids in sequence4.txt instead of manually putting them in list
with open("sequence4.txt") as file:
    for line in file:
        line = line.strip()
        if line:
            given_ids.append(line)

location(given_ids)