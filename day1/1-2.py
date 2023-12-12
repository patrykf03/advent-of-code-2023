import regex as re
import sys

with open(sys.argv[1]) as file:
    print(
        sum([
            int((lambda digits: digits[0] + digits[-1])(re.sub(
                "one", "1",
                re.sub(
                    "two", "2",
                    re.sub(
                        "three", "3",
                        re.sub(
                            "four", "4",
                            re.sub(
                                "five", "5",
                                re.sub(
                                    "six", "6",
                                    re.sub(
                                        "seven", "7",
                                        re.sub(
                                            "eight", "8",
                                            re.sub(
                                                "nine", "9", "".join(
                                                    re.findall(
                                                        "1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine",
                                                        currLine,
                                                        overlapped=True))))))))))))) for currLine in file
        ]))
