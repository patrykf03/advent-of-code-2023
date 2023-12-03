import regex as re
import sys

with open(sys.argv[1]) as file:
    partMatrix = []  # the whole schematic as an array of strings (For regex lmfao)
    symbols = []  # symbols we found
    partSum = 0
    for row, line in enumerate(file):  # going through every row to find coords of symbols (and append the row)
        partMatrix.append(line)  # append current row
        for col, lineCharacter in enumerate(line):  # go through every character
            if (lineCharacter in r"""!"#$%&'()*+,-/:;<=>?@[\]^_`{|}~"""):  # check if its a special
                symbols.append((row, col))  # add to list of specials
    for row, col in symbols:  # go over every special
        for nearSymbolRow in range(row - 1, row + 2):  # go over the 3 rows that surround the special
            for foundNumber in re.finditer("\d+", partMatrix[nearSymbolRow]):  # go over every number in row
                if col in set(range(*(tuple(map(sum, zip(foundNumber.span(), (-1, +1))))))):  # check if special is in the number +/- 1 position
                    partSum += int(foundNumber.group())  # add to sum if it is
    print(partSum)