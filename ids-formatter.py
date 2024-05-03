import json
import re

data = {}
with open("data/ids-cdp.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        _, kanji, *ids = line.split()
        for i in range(len(ids)):
            ids[i-1] = re.sub(r'\[.*?\]', '', ids[i-1])
        data[kanji] = ids
    
with open("data/UCSkanji.json", mode="w", encoding="utf-8") as g:
    g.write(json.dumps(data,indent=4))
