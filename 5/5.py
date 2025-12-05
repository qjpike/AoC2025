def is_ing(num, ingredients):
    for l,r in ingredients:
        if num < l:
            continue
        if num > r:
            continue
    
        return (l,r)
    return None


with open("input.txt") as f:
    inp = [i.strip() for i in f.readlines()]

ing_set = []

for i in inp:
    if i == "":
        break
    l = int(i.split("-")[0])
    r = int(i.split("-")[1])
    ing_set.append((l,r))

ing_set.sort()
combined_sets = [ing_set[0]]

for l, r in ing_set[1:]:
    low = is_ing(l, combined_sets)
    high = is_ing(r, combined_sets)

    if low is None and high is None:
        combined_sets.append( (l, r) )
    elif low is not None and high is None:
        combined_sets[combined_sets.index(low)] = (low[0], r)

# Part One
spoiled_count = 0
for i in inp:
    if "-" in i or i == "":
        continue
    spoiled_count += 1 if is_ing(int(i), combined_sets) is not None else 0

# Part Two
ing_count = 0
for l, r in combined_sets:
    ing_count += (r - l) + 1

print("Part One:", spoiled_count)
print("Part Two:", ing_count)