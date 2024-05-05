import json
import re

inputfile = "data/UCSkanji-smashed.json"
outputfile = "data/UCSkanji-tree.json"
# inputfile = "data/joyo-smashed.json"
# outputfile = "data/joyo-tree.json"
# inputfile = "data/test.json"
# outputfile = "data/test-tree.json"

data = {}
with open(inputfile, mode="r", encoding="utf-8") as f:
    data = json.load(f)

def ids_split(ids):
    return re.findall(r'[^&]|&.*;', ids)

tree = {}
for kanji in data:
    ids = data[kanji]
    ids_ary = ids_split(ids)
    current_elem = tree
    for i in range(len(ids_ary)-1):
        if ids_ary[i] not in current_elem:
            current_elem[ids_ary[i]] = {}
        current_elem = current_elem[ids_ary[i]]
    current_elem[ids_ary[-1]] = kanji

with open(outputfile, mode="w", encoding="utf-8") as g:
    g.write(json.dumps(tree))
