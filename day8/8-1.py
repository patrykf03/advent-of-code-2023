import sys
import re

# load input as array of strings
with open(sys.argv[1]) as file:
    taskInput = file.read()

originalMoves = taskInput.split('\n')[0]
nodes = dict([
    tuple([
        foundItems[0] if len(foundItems := re.findall(r"(\w+)", nodeItem)) == 1
        else tuple(foundItems) for nodeItem in nodeLine.split('=')
    ]) for nodeLine in taskInput.split('\n')[2::]
])


def applyMoves(moves, startingNode):
    currentNode = startingNode
    stepCount = 0
    for move in moves:
        if currentNode == 'ZZZ':
            break
        else:
            stepCount += 1
            if move == 'R':
                currentNode = nodes.get(currentNode)[1]
            else:
                currentNode = nodes.get(currentNode)[0]
    return currentNode, stepCount


totalSteps = 0
currentNode = 'AAA'
while currentNode != 'ZZZ':
    currentNode, currentSteps = applyMoves(originalMoves, currentNode)
    totalSteps += currentSteps
    print(
        f"re-applying moveset as finished at {currentNode}, step count {totalSteps}"
    )
