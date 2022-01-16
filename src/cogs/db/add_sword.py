import json

questions = [
    "What is sword name?",
    "How it cost?",
    "How much damage it dealt?",
    "How rare it is? (Common, Default, Rare)",
    "What material it made of? (Iron, Diamond, Gold, Stone, Wood, Leather, Bone) (Split every material with a comma)",
]

answer = []

for question in questions:
    answer.append(input(question + ":\n"))

with open("src/cogs/db/blacksmith.json") as fp:
    db = json.load(fp)

b = []

for material in answer[4].split(","):
    b.append(material.strip().lower())

db["swords"].append(
    {
        "name": answer[0].lower(),
        "cost": answer[1],
        "damage": answer[2],
        "rareness": answer[3],
        "material": b,
        "health": 100,
    }
)

with open("src/cogs/db/blacksmith.json", "w") as fp:
    json.dump(db, fp, indent=4)
