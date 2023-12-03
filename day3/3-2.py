import regex as re
import sys

with open(sys.argv[1]) as file:
    partMatrix = []  # the whole schematic as an array of strings (For regex lmfao)
    symbols = []  # gears we found
    partSum = 0
    for row, line in enumerate(file):  # going through every row to find coords of symbols (and append the row)
        partMatrix.append(line)  # append current row
        for col, lineCharacter in enumerate(line):  # go through every character
            if (lineCharacter == "*"):  # check if its a gear
                symbols.append((row, col))  # add to list of gears
    for row, col in symbols:  # go over every gear
        foundSpecials = [] # note the parts connected to gear
        for nearSymbolRow in range(row - 1, row + 2):  # go over the 3 rows that surround the special
            for foundNumber in re.finditer("\d+", partMatrix[nearSymbolRow]):  # go over every number in row
                if col in set(range(*(tuple(map(sum, zip(foundNumber.span(), (-1, +1))))))):  # check if special is in the number +/- 1 position
                    foundSpecials.append(foundNumber.group()) # add to connected list
        if len(foundSpecials) == 2: # check if gear has 2 parts
            partSum += int(foundSpecials[0])*int(foundSpecials[1]) # add gear ratio
    print(partSum)