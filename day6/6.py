from functools import reduce
from operator import mul

file = 'input.txt'

# load input as array of strings
with open(file) as file:
    taskInput = file.readlines()

races = (list(zip((races := [line.split(':')[1].split() for line in taskInput])[0], races[1])))

race = list(map(int, [line.split(':')[1].strip().replace(' ', '') for line in taskInput]))  # list of lists of strings

print(
    f"part 1: {reduce(mul,[len([distance for holdTime in range(1,int(race[0])+1) if (distance := holdTime*(int(race[0]) - holdTime)) > int(race[1])]) for race in races])}"
)

print(
    f"part 2: {len([distance for holdTime in range(1,race[0]+1) if (distance := holdTime*(race[0] - holdTime)) > race[1]])}"
)
