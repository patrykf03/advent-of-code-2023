import regex as re
import sys

with open(sys.argv[1]) as file:
    partMatrix = file.readlines()  # the whole schematic as an array of strings (For regex lmfao)
    symbols = []  # gears we found
    partSum = 0 # sum of gear ratios
    symbols = [
        (row, col) # symbol coords
        for row, line in enumerate(partMatrix)  # go over every row
        for col, lineCharacter in enumerate(line)  # go over every character
        if lineCharacter == "*" # check if its a gear
    ]
    for row, col in symbols:  # go over every gear
        foundSpecials = [
            int(foundNumber.group())  # note the parts connected to gear
            for nearSymbolRow in range(row - 1, row + 2)  # go over the 3 rows that surround the gear
            for foundNumber in re.finditer("\d+", partMatrix[nearSymbolRow])  # go over every number in row
            if col in set(range(*(map(sum, zip(foundNumber.span(), (-1, +1))))))  # check if gear is in the number +/- 1 position
        ]
        if len(foundSpecials) == 2:  # check if gear has 2 parts
            partSum += foundSpecials[0] * foundSpecials[1]  # add gear ratio
    print(partSum)
