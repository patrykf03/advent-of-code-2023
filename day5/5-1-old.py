import sys


# load input as array of strings
with open(sys.argv[1]) as file:
    taskInput = file.read()

print("splitting data")
puzzleData = taskInput.split("\n\n")

print("splitting seeds")
seeds = puzzleData[0].split()[1:]
print("getting location")
lowestLocation = int(seeds[0])

dictList = []

# 0  seedToSoil
# 1  soilToFertilizer
# 2  fertilizerToWater
# 3  waterToLight
# 4  lightToTemperature
# 5  temperatureToHumidity
# 6  humidityToLocation


print("generating dictionaries")
for mapId, map in enumerate(puzzleData[1:]):
    print(f"dictionary {mapId}")
    map = [number.split() for number in map.split("\n")[1:]]
    currentDict = {}
    for mapLine in map:
        mapLine = [int(a) for a in mapLine]

        destinationList = list(range(mapLine[0],mapLine[0]+mapLine[2]))
        sourceList = list(range(mapLine[1],mapLine[1]+mapLine[2]))

        currentDict = currentDict | {sourceList[i]:destinationList[i] for i in range(len(sourceList))}
    dictList.append(currentDict)

for seedNumber in seeds:
    print(seedNumber)
    print(seedNumber)
    currentNumber = int(seedNumber)

    for mapId in range(len(dictList)):
        currentNumber = dictList[mapId].get(currentNumber,currentNumber)
    if currentNumber < lowestLocation:
        lowestLocation = currentNumber

print(lowestLocation)
