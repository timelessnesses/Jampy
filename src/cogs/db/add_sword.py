import json

questions = [
	"What is sword name?",
	"How it cost?",
	"How much damage it dealt?",
	"How rare it is? (Common, Default, Rare)"
]

answer = []

for question in questions:
	answer.append(input(question+":\n"))

with open("blacksmith.json") as fp:
	db = json.load(fp)

db["swords"].append({
	"name":answer[0],
	"cost":answer[1],
	"damage":answer[2],
	"rareness":answer[3]
})