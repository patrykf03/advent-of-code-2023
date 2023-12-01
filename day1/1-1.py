import re

with open("input.txt") as file:
    print(
        sum(
            [
                int((lambda digits: digits[0] + digits[-1])(re.findall("\d", currLine)))
                for currLine in file
            ]
        )
    )
