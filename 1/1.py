with open("input.txt") as f:
    inp = f.readlines()

moves = []
for i in inp:
    moves.append((i[0], int(i[1:])))

cur_loc = 50
answer_count_1 = 0
answer_count_2 = 0

plant_set = set()
plant_set.add(0)

wrap_set = set()
for i in range(-1100, 1100, 100):
    wrap_set.add(i)

for dir, count in moves:
    if dir == "R":
        new_range = set(range(cur_loc + 1, cur_loc + count + 1))
        cur_loc += count
    elif dir == "L":
        new_range = set(range(cur_loc - count, cur_loc))
        cur_loc -= count
    cur_loc %= 100

    answer_count_1 += 1 if cur_loc == 0 else 0
    answer_count_2 += len(wrap_set.intersection(new_range))

print("Part One:", answer_count_1)
print("Part Two:", answer_count_2) 