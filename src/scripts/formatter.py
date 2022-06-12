#used to format the poem into json

from flask import jsonify
import json

poem = []
length = 0

with open("src/data/poem.txt", "r") as file:
    for line in file:
        poem.append(line)
        length += 1

json_poem = json.dumps(poem)
print(json_poem)
with open("src/json/poem.json", "w") as res:
    res.write(json_poem)
with open("src/json/size.json", "w") as res:
    res.write(json.dumps(length))