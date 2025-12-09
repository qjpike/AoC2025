from collections import defaultdict

with open("input.txt") as f:
    inp = [i.strip() for i in f.readlines()]

splitter_set = set()
beam_dict = defaultdict(int)

for y, row in enumerate(inp):
    for x, char in enumerate(row):
        if char == "S":
            beam_dict[(x,y+1)] = 1
        elif char == "^":
            splitter_set.add((x,y))

splits = 0
for _ in inp:
    new_beam_dict = defaultdict(int)
    for (x,y), count in beam_dict.items():
        if (x, y+1) in splitter_set:
            splits += 1    
            new_beam_dict[(x-1, y+1)] += count
            new_beam_dict[(x+1, y+1)] += count
        else:
            new_beam_dict[(x, y+1)] += count

    beam_dict = new_beam_dict

print("Part One:", splits)
print("Part Two:", sum(beam_dict.values()))
