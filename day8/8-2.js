const { once } = require('events');
const fs = require('fs');

// load input as string
const taskInput = fs.readFileSync('input.txt', 'utf8');

const originalMoves = taskInput.split('\n')[0];
const nodes = {};
taskInput.split('\n').slice(2).forEach(nodeLine => {
  const foundItems = nodeLine.split('=');
  const nodeKey = foundItems[0].trim();
  const nodeValue = [...foundItems[1].match(/(\w+)/g)];
  nodes[nodeKey] = nodeValue;
});

function applyMoves(moves, startingNodes) {
  let currentNodes = startingNodes;
  let stepCount = 0;
  for (const move of moves){
    stepCount++;
    if (currentNodes.every(node => node[2] === 'Z')) {
      break;
    }
    currentNodes = currentNodes.map(node => {
      if (move === 'R') {
        return nodes[node][1]
      } else {
        return nodes[node][0]
      }
    });
  }
  return [currentNodes, stepCount];
}

let totalSteps = 0;
let currentNodes = Object.keys(nodes)
  .filter((key) => key[2] === "A")
const oneCycleLength = originalMoves.length;

while (!(currentNodes.every(node => node[2] == 'Z'))) {
  [currentNodes, currentSteps] = applyMoves(originalMoves, currentNodes);
  totalSteps += currentSteps;
  if (totalSteps % (4000 * oneCycleLength) === 0) {
    console.log(totalSteps);
  }
}

console.log("FOUND")
console.log(currentNodes)