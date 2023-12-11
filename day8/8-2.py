import sys
import re
import math

# load input as array of strings
with open(sys.argv[1]) as file:
    taskInput = file.read()

moves = taskInput.split("\n")[0]
nodes = dict(
    [
        tuple(
            [
                foundItems[0]
                if len(foundItems := re.findall(r"(\w+)", nodeItem)) == 1
                else tuple(foundItems)
                for nodeItem in nodeLine.split("=")
            ]
        )
        for nodeLine in taskInput.split("\n")[2::]
    ]
)

sys.setrecursionlimit(100000000) # LMFAO

def countSteps(moves,startingNode,steps):
    currentNode = startingNode
    for move in moves:
        if currentNode[2] != 'Z':
            steps+=1
            if move == 'R':
                currentNode = nodes.get(currentNode)[1]
            else:
                currentNode = nodes.get(currentNode)[0]
    if currentNode[2] != 'Z':
        return countSteps(moves,currentNode,steps)
    else:
        return steps


totalSteps = 0
currentNodes = list(filter(lambda x: x[2] == "A", nodes))



cycleLength = math.lcm(*[countSteps(moves,node,0) for node in currentNodes])
print(cycleLength)