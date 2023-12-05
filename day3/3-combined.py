import regex as re
import sys

def findNumbersTouchingSpecial(row, col, parts):
    return [
        int(foundNumber.group())  # note the parts connected to special
        for nearSymbolRow in range(row - 1, row + 2)  # go over the 3 rows that surround the special
        for foundNumber in re.finditer("\d+", parts[nearSymbolRow])  # go over every number in row
        if col in set(range(*(map(sum, zip(foundNumber.span(), (-1, +1))))))  # check if special is in the number +/- 1 position
    ]

def getSymbolCoords(filter, parts):
    return [
        (row, col)  # symbol coords
        for row, line in enumerate(parts)  # go over every row
        for col, lineCharacter in enumerate(line)  # go over every character
        if lineCharacter in filter  # check if part in filter string
    ]

def getPart1(partList):
    return sum(
        sum(
            [
                findNumbersTouchingSpecial(row, col, partList)
                for row, col in getSymbolCoords(r"""!"#$%&'()*+,-/:;<=>?@[\]^_`{|}~""", partList)
            ],
            []
        )
    )

def getPart2(partList):
    return sum(
        [
            gears[0]*gears[1]
            for gears in [
                findNumbersTouchingSpecial(row, col, partList)
                for row, col in getSymbolCoords(r"*", partList)
            ]
            if len(gears) == 2
        ]
    )

with open(sys.argv[1]) as file:
    partMatrix = file.readlines() # the whole schematic as an array of strings (For regex lmfao)

# part 1 (sum of all numbers touching a special character)
print(f"part 1: {getPart1(partMatrix)}")
print(f"part 2: {getPart2(partMatrix)}")