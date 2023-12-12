import regex as re
import sys
from word2number import w2n

with open(sys.argv[1]) as file:
    print(
        sum([(lambda digits: w2n.word_to_num(digits[0]) * 10 + w2n.word_to_num(digits[-1]))(re.findall(
            "1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine",
            currLine,
            overlapped=True,
        )) for currLine in file]))
