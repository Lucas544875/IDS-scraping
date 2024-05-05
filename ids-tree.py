import json
import re

inputfile = "data/UCSkanji-smashed.json"
# outputfile = "data/UCSkanji-tree.json"
outputfile = "data/UCSkanji-tree-reverse.json"
# inputfile = "data/joyo-smashed.json"
# outputfile = "data/joyo-tree.json"
# outputfile = "data/joyo-tree-reverse.json"
# inputfile = "data/test.json"
# outputfile = "data/test-tree.json"
# outputfile = "data/test-tree-reverse.json"

data = {}
with open(inputfile, mode="r", encoding="utf-8") as f:
    data = json.load(f)

def ids_split(ids):
    return re.findall(r'[^&]|&.*;', ids)

tree = {}
for kanji in data:
    ids = data[kanji]
    ids_ary = ids_split(ids)
    ids_ary.reverse()
    current_elem = tree
    for i in range(len(ids_ary)):
        if ids_ary[i] not in current_elem:
            current_elem[ids_ary[i]] = {}
        current_elem = current_elem[ids_ary[i]]
    current_elem["terminal"] = kanji

with open(outputfile, mode="w", encoding="utf-8") as g:
    g.write(json.dumps(tree))
