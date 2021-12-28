import sys

# GLOBAL VARIABLES
MOVES = {'S': (1, 0), 'E': (0, 1), 'N': (-1, 0), 'W': (0, -1)}
DIRECTION_STRING = {'S': 'SOUTH', 'E': 'EAST', 'N': 'NORTH', 'W': 'WEST'}

# World variable
world = []

# Blunder variables
arrived = False
direction_priorities = 'SENW'
drunk = False
current_direction = 'S'
memory = set()
movements = []

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, c = [int(i) for i in input().split()]
for i in range(l):
    line = input()
    if '@' in line:
        blunder_x = i
        blunder_y = line.index('@')
    world += list(line)

def world_string(l, c, world):
    res = ""
    for i in range(l):
        for j in range(c):
            res += world[i*c+j]
    return res

def get_other_teleporter(x, y, l, c, world):
    for i in range(l):
        for j in range(c):
            if world[i*c+j] == "T" and (i != x or j != y):
                return i, j
    return -1, -1

def print_blunder_and_world(x, y, l, c, world):
    for i in range(l):
        line = ""
        for j in range(c):
            if i == x and j == y:
                line += "R"
            else: 
                line += world[i*c+j]
        print(line)

# f = open(sys.argv[1], "r")
# first_line = f.readline().split()
# l, c = int(first_line[0]), int(first_line[1])
# for i in range(l):
#     line = f.readline().replace('\n', '')
#     if '@' in line:
#         blunder_x = i
#         blunder_y = line.index('@')
#     world += list(line)

while not(arrived):
    # print_blunder_and_world(blunder_x, blunder_y, l, c, world)
    
    next_blunder_x = blunder_x + MOVES[current_direction][0]
    next_blunder_y = blunder_y + MOVES[current_direction][1]
    if drunk and world[next_blunder_x*c+next_blunder_y] == 'X':
        world[next_blunder_x*c+next_blunder_y] = ' '
    
    if world[next_blunder_x*c+next_blunder_y] in '#X':
        count = 0
        while world[next_blunder_x*c+next_blunder_y] in '#X':
            current_direction = direction_priorities[count]
            next_blunder_x = blunder_x + MOVES[current_direction][0]
            next_blunder_y = blunder_y + MOVES[current_direction][1]
            count  += 1

    blunder_x = next_blunder_x
    blunder_y = next_blunder_y
    movements += [DIRECTION_STRING[current_direction]]
    
    current_box = world[blunder_x*c+blunder_y]
    if current_box in 'SENW':
        current_direction = current_box
    elif current_box == 'B':
        drunk = not(drunk)
    elif current_box == 'I':
        direction_priorities = direction_priorities[::-1]
    elif current_box == 'T':
        blunder_x, blunder_y = get_other_teleporter(blunder_x, blunder_y, l, c, world)
    elif current_box == "$":
        arrived = True
    
    # Memorize all informations possible
    information = blunder_x, blunder_y, direction_priorities, current_direction, drunk, world_string(l, c, world)
    if information in memory:
        movements = ['LOOP']
        break
    else:
        memory.add(information)

print(*movements, sep='\n')
