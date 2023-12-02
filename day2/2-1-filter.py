import regex as re
import sys

with open(sys.argv[1]) as file:
    validSum = 0
    for gameNumber, gameResults in enumerate(file):
        isValid = True
        for move in re.sub('Game(.)*:', '', re.sub('\s', '', gameResults)).split(';'):
            for colour in move.split(','):
                if ('red' in colour) and (int(''.join(filter(str.isdigit, colour)))) > 12:
                    isValid = False
                if ('green' in colour) and (int(''.join(filter(str.isdigit, colour)))) > 13:
                    isValid = False
                if ('blue' in colour) and (int(''.join(filter(str.isdigit, colour)))) > 14:
                    isValid = False                            
        if isValid:
            validSum += gameNumber+1
    print(validSum)