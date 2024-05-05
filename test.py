import json
import re

data = {}
with open("data/UCSkanji-smashed.json", mode="r", encoding="utf-8") as f:
    data = json.load(f)


kanji = "\ud879\udf26"
print(kanji)
print(kanji,data[kanji])

# saro = "🌕の夜に𩸽食べたい"
# print(ids_split(saro))