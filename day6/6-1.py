from functools import reduce
from operator import mul

file = 'input.txt'

# load input as array of strings
with open(file) as file:
    taskInput = file.readlines()

races = [line.split(':')[1].split() for line in taskInput] # part 1 separate races
races = list(zip(races[0],races[1])) # list of tuples (Time,distance)

print(reduce(mul,[len([distance for holdTime in range(1,int(race[0])+1) if (distance := holdTime*(int(race[0]) - holdTime)) > int(race[1])]) for race in races]))

