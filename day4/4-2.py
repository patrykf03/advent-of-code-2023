import regex as re
import sys
from functools import cache

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
cardCount = 0  # total card (original and clone) count

# save scores
for id, scratchCard in enumerate(scratchCards):
    cardScore = 0  # card score
    for number in scratchCard[1]:
        if number in scratchCard[0]:
            cardScore += 1
    cardScores[id] = cardScore

# make clone cards and return the sum of everything under
@cache
def recurseCount(n):
    count = 1  # Initialize count with 1 for the current card
    # Run recursion for every new clone card
    for m in range(cardScores[n]):
        count += recurseCount(n + m + 1)
    return count

totalCardCount = 0  # Initialize total card count

# Run recursion on winning original cards and add 1 for non-winning cards
for cardId, cardScore in enumerate(cardScores):
    if cardScore != 0:
        totalCardCount += recurseCount(cardId)
    else:
        totalCardCount += 1

print(totalCardCount)
