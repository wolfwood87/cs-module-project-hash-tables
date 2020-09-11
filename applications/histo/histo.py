# Your code here

import re

with open("robin.txt") as f:
    robin = f.read()

def histo(s):
    hash_count = {}
    # Your code here
    words = s.split()
    for word in words:
        word = re.sub("[^A-Za-z0-9']+", '', word)
        lower = word.lower()
        if f"{lower}" in hash_count:
            hash_count[f"{lower}"] += "#"
        elif word != "":
            hash_count[f"{lower}"] = "#"
    return hash_count

hash_count = sorted(histo(robin).items(), key=lambda x: (x[1], x[0]), reverse=True)

for hash in hash_count:
    print(f"{hash[0]}  {hash[1]}")