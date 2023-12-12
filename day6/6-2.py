    file = 'input.txt'

# load input as array of strings
with open(file) as file:
    taskInput = file.readlines()

race = [line.split(':')[1].strip().replace(' ', '') for line in taskInput]  # list of lists of strings
print(
    len([
        distance for holdTime in range(1,
                                       int(race[0]) + 1)
        if (distance := holdTime * (int(race[0]) - holdTime)) > int(race[1])
    ]))
