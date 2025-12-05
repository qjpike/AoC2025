from copy import deepcopy as dc

with open("input.txt") as f:
    inp = [i.strip() for i in f.readlines()]

field = set()
max_x = 0
max_y = 0
surrounds = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

for y, row in enumerate(inp):
    for x, char in enumerate(row):
        if char == "@":
            field.add((x,y))

old_count = len(field)
first_time = True
count = 0

while True:
    new_field = dc(field)

    for x,y in list(field):
        check_set = [(x + dx, y + dy) for dx, dy in surrounds]
        if len(field.intersection(set(check_set))) < 4:
            new_field.remove((x,y))

    if new_field == field:
        break
    if first_time:
        print("Part One:", old_count - len(new_field))
        first_time = False
    field = new_field

print("Part Two:", old_count - len(field)) 
