import sys

# load input as array of strings
with open(sys.argv[1]) as file:
    taskInput = file.readlines()

reports = [[int(y.strip()) for y in x.split()] for x in taskInput]

estimationSum = 0

for reportLine in reports:
    allLines = [reportLine]
    while not all(map(lambda x: x == 0, allLines[-1])):
        allLines.append(list(map((lambda x: x[1] - x[0]), zip(allLines[-1], allLines[-1][1::]))))

    # reverse allLines and add a 0 to the end of every line
    allLines = list(map(lambda x: x + [0], allLines))[::-1]

    for lineNum in range(len(allLines)):
        if lineNum != 0:
            allLines[lineNum][-1] = allLines[lineNum][-2] + allLines[lineNum - 1][-1]

    #prettyprint with padding
    print("\n\n")
    print("\n".join(
        list(
            map(
                lambda xs: str([str(x).center(8, '_') for x in xs]).replace("'", "").replace(",", "").replace(
                    " ", "        ").center(350, '.'), allLines))))
    estimationSum += allLines[-1][-1]

print("====================================================")
print(estimationSum)

25520678
