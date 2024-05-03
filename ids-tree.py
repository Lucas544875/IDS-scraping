import json
import re

inputfile = "data/joyo.json"
outputfile = "data/joyo-smashed.json"
# inputfile = "data/UCSkanji.json"
# outputfile = "data/UCSkanji-smashed.json"

data = {}
with open(inputfile, mode="r", encoding="utf-8") as f:
    data = json.load(f)

def ids_split(ids):
    return re.findall(r'[^&]|&.*;', ids)

def ids_rec(char, data, level=0):
    if char not in data:
        return char
    ids = data[char][0]
    if len(ids) == 1:
        return char
    ids_ary = [ids_rec(c, data, level+1) for c in ids_split(ids)]
    return "".join(ids_ary)

data_smashed = {}

for k in data:
    data_smashed[k] = ids_rec(k, data)

with open(outputfile, mode="w", encoding="utf-8") as g:
    g.write(json.dumps(data_smashed,indent=4))
