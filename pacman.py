# Name: Aylwin Sim
# Project: https://github.com/ie/Code-Challenge-1

def move_south_east(step):
    return step+1
def move_north_west(step):
    return step-1

def move(x, y):
    if(facing == 'EAST' and move_south_east(x)<5): x = move_south_east(x)
    if(facing == 'WEST' and move_north_west(x)>=0): x = move_north_west(x)
    if(facing == 'NORTH' and move_north_west(y)>=0): y = move_north_west(y)
    if(facing == 'SOUTH' and move_south_east(y)<5): y = move_south_east(y)
    return x, y

def report():
    print(f'Output: {x},{4-y},{facing}')
    with open(FILE, 'a+') as f:
        f.write(f'\n\nOutput: {x},{4-y},{facing}')
    return f'Output: {x},{4-y},{facing}'

def change_facing(position):
    if position=='LEFT': return DIRECTIONS[DIRECTIONS.index(facing)-1%4]
    if position=='RIGHT': return DIRECTIONS[DIRECTIONS.index(facing)+1%4]

def place(str):
    place = str.replace('PLACE ', '').replace('\n', '').split(',')
    x = int(place[0])
    y = 4-int(place[1])
    facing = place[2].upper()
    return x, y, facing

DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']
FILE = 'case_1.txt' # Change the FILE name to different cases

with open(FILE) as f:
    lines = f.readlines()
        
if(lines[0].upper().startswith('PLACE')):
    for line in lines:
        if(line!='\n'):
            if 'PLACE' in line: x, y, facing = place(line)
            if 'MOVE' in line: x, y = move(x, y)
            if 'LEFT' in line: facing = change_facing('LEFT')
            if 'RIGHT' in line: facing = change_facing('RIGHT')
            if 'REPORT' in line: report()
else:
    print('Invalid First Command')