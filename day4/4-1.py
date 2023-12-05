import regex as re
import sys


# load input as array of strings
with open(sys.argv[1]) as file:
    taskInput = file.readlines()

# parse input into a list of tuplets (winning, given)
scratchCards = [
    re.findall("\d+", part)
    for card in taskInput
    for part in card.split(":")[1].split("|")
]
scratchCards = list(zip(scratchCards[::2], scratchCards[1::2]))

globalScore = 0  # overall score

for scratchCard in scratchCards:
    cardScore = 0
    for number in scratchCard[1]:
        if number in scratchCard[0]:
            if cardScore == 0:
                cardScore += 1
            else:
                cardScore = cardScore * 2
    globalScore += cardScore
print(globalScore)