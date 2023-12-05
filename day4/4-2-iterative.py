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

cardScores = [0] * (len(scratchCards))  # per card score list
stack = []  # card processing stack
cardCount = 0  # final card count

# save scores and push winning cards to stack
for id, scratchCard in enumerate(scratchCards):
    cardScore = 0  # current card score
    for number in scratchCard[1]:  # check for matches
        if number in scratchCard[0]:
            cardScore += 1
    cardScores[id] = cardScore  # add score to list
    if cardScore != 0:  # add card to stack if it has a score
        stack.append(id)
    else:  # add as a non winning card otherwise
        cardCount += 1

# process stack to make clones which will also be processed
while stack:
    n = stack.pop()
    cardCount += 1
    if cardScores[n] != 0:
        for m in range(cardScores[n]):
            stack.append(n + m + 1)


print(cardCount)