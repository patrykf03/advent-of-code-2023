import regex as re
import sys

# set up starting variables
with open(sys.argv[1]) as file:  # load input as array of strings
    partMatrix = file.readlines()
gearRatioSum = 0

symbols = [
    (row, col)  # symbol coords
    for row, line in enumerate(partMatrix)  # go over every row
    for col, lineCharacter in enumerate(line)  # go over every character
    if lineCharacter == "*"  # check if its a gear
]

for row, col in symbols:  # go over every gear
    touchingNumbers = [  # get the numbers touching the gear
        int(foundNumber.group())
        for row, col in symbols  # go over every special
        for nearSymbolRow in range(row - 1, row + 2)  # go over the 3 rows that surround the special
        for foundNumber in re.finditer("\d+", partMatrix[nearSymbolRow])  # go over every number in row
        if col in set(range(
            *(map(sum, zip(foundNumber.span(), (-1, +1))))))  # check if special is in the number +/- 1 position
    ]
    if len(touchingNumbers) == 2:  # if there are 2 numbers touching the gear then add gear ratio to sum
        gearRatioSum += touchingNumbers[0] * touchingNumbers[1]

print(gearRatioSum)
