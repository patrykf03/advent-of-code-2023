import sys

# load input as array of strings
with open(sys.argv[1]) as file:
    taskInput = file.read()

# all of the data split along empty lines
puzzleData = taskInput.split("\n\n")

seeds = [int(n) for n in puzzleData[0].split()[1:]] # get the seeds
lowestLocation = seeds[0] # set the lowest seed to the first seed


# get the list of maps
maps = [[number.split() for number in map.split("\n")[1:]] for map in puzzleData[1:]]

# function to get the Location that maps to the seed
def getLocation(maps,seed):
    currentNumber = int(seed)
    for map in maps:
        for mapLine in map:
            destStart = int(mapLine[0])
            sourceStart = int(mapLine[1])
            mapLineLength = int(mapLine[2])
            if (sourceStart <= currentNumber <= (sourceStart+mapLineLength-1)):
                currentNumber = destStart+(currentNumber-sourceStart)
                break
    return currentNumber

# finding the lowest seed
for seed in seeds:
    currentLocation = getLocation(maps,seed)
    if currentLocation < lowestLocation:
        lowestLocation = currentLocation

print(lowestLocation)
