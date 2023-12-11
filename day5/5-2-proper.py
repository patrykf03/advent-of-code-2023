import sys
from copy import deepcopy

# load input as array of strings
with open(sys.argv[1]) as file:
    taskInput = file.read()

puzzleData = taskInput.split("\n\n")

seedsLists = puzzleData[0].split()[1:]
seedsLists = list(
    zip(
        [int(num) for num in seedsLists[::2]],
        [int(m) + int(n) - 1 for m, n in zip(seedsLists[::2], seedsLists[1::2])],
    ),
)

# convert to list of (sourceStart,sourceEnd,destStart)
maps = [
[
        tuple([
                int(number.split()[1]),
                int(number.split()[1]) + int(number.split()[2]) - 1,
                int(number.split()[0])]
        )
        for number in map.split("\n")[1:]
    ]
    for map in puzzleData[1:]
]


def applyOffset(sourceStart, destStart, range):
    return tuple([destStart + (rangeNumber - sourceStart) for rangeNumber in range])


def splitRangeAlongMap(sourceStart, sourceEnd, range):
    before = (-1, -1)
    middle = (-1, -1)
    after = (-1, -1)

    # check if we start before the map conversion starts but also end in the range
    if range[0] < sourceStart and range[1] >= sourceStart:
        # check if we go outside the map conversion area on the other side (3 way split)
        if range[1] > sourceEnd:
            # triple overlap, map range is in the middle of the provided range
            before = tuple([range[0], sourceStart - 1])
            middle = tuple([sourceStart, sourceEnd])
            after = tuple([sourceEnd + 1, range[1]])
            return [before, middle, after]
        else:
            # partial overlap from left side, split into mappable and non mappable (in this MapLine) parts
            before = tuple([range[0], sourceStart - 1])
            middle = tuple([sourceStart, range[1]])
            return [before, middle, after]

    # check if we end after the map conversion starts but also start in the range
    elif range[1] > sourceEnd and range[0] <= sourceEnd:
        # we go out the other side
        middle = tuple([range[0], sourceEnd])
        after = tuple([sourceEnd + 1, range[1]])
        return [before, middle, after]

    # check if we are fully inside the map conversion
    elif range[0] >= sourceStart and range[1] <= sourceEnd:
        middle = tuple([range[0], range[1]])
        return [before, middle, after]

    # check if we are fully outside the map conversion
    else:
        # we are fully outside the mapline (no match)
        return [before, middle, after]


def applyMapToRanges(mapLines, inputRanges):
    procesStack = inputRanges  # preset process stack with initial ranges

    outputRanges = []  # store output ranges post conversion

    # go over all provided ranges and the ones given later
    while procesStack:
        range = procesStack.pop()  # get new range
        for mapLine in mapLines:  # go over every map conversion option for this range
            sourceStart = mapLine[0]
            sourceEnd = mapLine[1]
            destStart = mapLine[2]

            # split range into parts that are before, during and after the map conversion
            splitRanges = splitRangeAlongMap(sourceStart, sourceEnd, range)

            # push the other parts to the stack to be reprocessed
            if splitRanges[0] != (-1, -1):
                procesStack.append(splitRanges[0])
            if splitRanges[2] != (-1, -1):
                procesStack.append(splitRanges[2])

            # add offset part to output and break out of mapline loop to go to next range
            if splitRanges[1] != (-1, -1):
                outputRanges.append(applyOffset(sourceStart, destStart, splitRanges[1]))
                break
            else:
                # if we are at the last mapline and we didnt add anything, add the range without offset
                if mapLine == mapLines[-1]:
                    outputRanges.append(range)

    return outputRanges


def part2(maps, seedLists):
    currentRanges = deepcopy(seedLists)
    for map in maps:
        currentRanges = applyMapToRanges(map, currentRanges)
    return min(list(zip(*currentRanges))[0])


print(part2(maps, seedsLists))
