#used to format the poem into json

from flask import jsonify
import json

poem = []

with open("src/data/poem.txt", "r") as file:
    for line in file:
        poem.append(line)

json_poem = json.dumps(poem)
print(json_poem)
with open("src/json/poem.json", "w") as res:
    res.write(json_poem)