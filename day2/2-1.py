import regex as re
import sys

with open(sys.argv[1]) as file:
    validSum = 0
    for gameNumber, gameResults in enumerate(file):
        isValid = True
        for move in re.sub('Game(.)*:', '', re.sub('\s', '', gameResults)).split(';'):
            for colour in move.split(','):
                if ('red' in colour):
                    if (int(re.findall('\d*(?=red)', colour)[0])) > 12:
                        isValid = False
                if ('green' in colour):
                    if (int(re.findall('\d*(?=green)', colour)[0])) > 13:
                        isValid = False
                if ('blue' in colour):
                    if (int(re.findall('\d*(?=blue)', colour)[0])) > 14:
                        isValid = False                 
        if isValid:
            validSum += gameNumber+1
    print(validSum)
