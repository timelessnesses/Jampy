import json

questions = [
	"What is sword name?",
	"How it cost?",
	"How much damage it dealt?",
	"How rare it is? (Common, Default, Rare)",
	"What material it made of? (Iron, Steel, Diamond, Gold, Stone, Wood, Leather, Bone) (Split every material with a comma)",
]

answer = []

for question in questions:
	answer.append(input(question+":\n"))

with open("blacksmith.json") as fp:
	db = json.load(fp)

db["swords"].append({
	"name":answer[0].lower(),
	"cost":answer[1],
	"damage":answer[2],
	"rareness":answer[3],
	"material":answer[4].split(",")
})