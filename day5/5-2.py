import sys

# load input as array of strings
with open(sys.argv[1]) as file:
    taskInput = file.read()

puzzleData = taskInput.split("\n\n")

seedsLists = puzzleData[0].split()[1:]
seedsLists = list(zip(seedsLists[::2], [int(m)+int(n) for m,n in zip(seedsLists[::2],seedsLists[1::2])]))

maps = [[number.split() for number in map.split("\n")[1:]] for map in puzzleData[1:]]

def getSeed(maps, location):
    currentNumber = location
    for map in maps[::-1]: # go through maps in reverse order
        for mapLine in map:
            # get source from dest
            destStart = int(mapLine[0])
            sourceStart = int(mapLine[1])
            rangeLength = int(mapLine[2])
            if (destStart <= currentNumber <= (destStart+rangeLength)-1):
                currentNumber = sourceStart+(currentNumber-destStart)
                break 
    return currentNumber

# reverse bruteforce the mf
currentLocation = 0
# check if found
found = False

while found != True:
    currentLocation+=1 # add 1 to get next
    # get seed from curent location
    seed = getSeed(maps, currentLocation)
    # check if our seed is in any of the seeds
    for givenSeed in seedsLists:
        if int(givenSeed[0]) <= seed <= givenSeed[1]:
            found=True
            break
print(currentLocation)