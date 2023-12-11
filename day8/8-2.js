import {nanomemoize as memoize} from 'nano-memoize';
import fs from 'fs';

// load input as string
const taskInput = fs.readFileSync('input.txt', 'utf8');

const moves = taskInput.split('\n')[0];
const nodes = {};
    taskInput.split('\n').slice(2).forEach(nodeLine => {
  const foundItems = nodeLine.split('=');
  const nodeKey = foundItems[0].trim();
  const nodeValue = [...foundItems[1].match(/(\w+)/g)];
  nodes[nodeKey] = nodeValue;
});

function applyMovesSingle(startingNode) {
  let currentNode = startingNode
  let stepCount = 0
  for (const move of moves){
    stepCount++;
    if (move === 'R') {
      currentNode = nodes[currentNode][1]
    } else {
      currentNode = nodes[currentNode][0]
    };
  };
  return [stepCount,currentNode];
}

const applyMovesSingleMemoized = memoize(applyMovesSingle)

function applyMoves(startingNodes) {
  let currentNodes = startingNodes;
  let stepCount = 0;

  for (const currentNode of currentNodes) {
    let newResult;
    newResult = applyMovesSingleMemoized(currentNode);
    stepCount += newResult[0];
    currentNodes[currentNodes.indexOf(currentNode)] = newResult[1];
  };
  stepCount = stepCount / startingNodes.length
  return stepCount;
}



let totalSteps = 0;
let currentNodes = Object.keys(nodes)
  .filter((key) => key[2] === "A")
const oneCycleLength = moves.length;


while (!(currentNodes.every(node => node[2] == 'Z'))) {
  totalSteps += applyMoves(currentNodes);
  if (totalSteps % (10000 * oneCycleLength) === 0) {
    console.log(totalSteps);
  }
}

console.log("FOUND");
console.log(totalSteps);