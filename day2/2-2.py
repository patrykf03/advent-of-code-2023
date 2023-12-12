import regex as re
import sys

with open(sys.argv[1]) as file:
    powerSum = 0
    for gameNumber, gameResults in enumerate(file):
        minValues = [0, 0, 0]
        for move in re.sub('Game(.)*:', '', re.sub('\s', '', gameResults)).split(';'):
            for colour in move.split(','):
                if 'red' in colour:
                    value = int((re.findall('\d*(?=red)', colour))[0])
                    if value > minValues[0]:
                        minValues[0] = value
                if 'green' in colour:
                    value = int((re.findall('\d*(?=green)', colour))[0])
                    if value > minValues[1]:
                        minValues[1] = value
                if 'blue' in colour:
                    value = int((re.findall('\d*(?=blue)', colour))[0])
                    if value > minValues[2]:
                        minValues[2] = value
        powerSum += minValues[0] * minValues[1] * minValues[2]
    print(powerSum)
