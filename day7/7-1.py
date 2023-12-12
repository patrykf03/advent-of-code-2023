import sys

# load input as array of strings
with open(sys.argv[1]) as file:
    taskInput = file.read()

# change task input to tuples of (hand,win)
bidDict = {hand: int(bid) for hand, bid in zip(taskInput.split()[::2], taskInput.split()[1::2])}

# make character swap translation table
letterMapTrans = str.maketrans({
    "A": "M",
    "K": "L",
    "Q": "K",
    "J": "J",
    "T": "I",
    "9": "H",
    "8": "G",
    "7": "F",
    "6": "E",
    "5": "D",
    "4": "C",
    "3": "B",
    "2": "A",
})
# change hand letters to alphabetical (for 2nd sort)
bidDictTranslated = {(key.translate(letterMapTrans)): value for key, value in bidDict.items()}


# give rank for a bid
def getBidRank(bid):
    rankDict = {5: 7, 4: 6, 3: 4, 2: 2}
    # count how many times every char happens
    occurenceCount = list(map(bid.count, set(bid)))

    # check for full house
    if {2, 3} <= set(occurenceCount):
        return 5
    # check for 2 pairs
    elif occurenceCount.count(2) == 2:
        return 3
    # "N of a kind check (and one pair)"  + translate to proper value
    elif (topCount := {max(occurenceCount)}) <= set(rankDict.keys()):
        return rankDict.get(*topCount)
    # otherwise high card
    else:
        return 1


# sort by getBidRank and then alphabetically and then calculate winnings and add together
print(
    sum([
        bid[0] * bidDictTranslated.get(bid[1])
        for bid in enumerate(sorted(bidDictTranslated, key=lambda k: (getBidRank(k), k)), 1)
    ]))
