with open("input.txt") as f:
    inp = [i.strip() for i in f.readlines()]

# string is an array of numbers
def find_next_value_recursive(string, char_num):
    if char_num == 1:
        max_val = max(string)
    else:
        max_val = max(string[:-(char_num-1)])
    next_string = string[string.index(max_val) + 1:]

    if char_num == 1:
        return str(max_val)
    return str(max_val) + find_next_value_recursive(next_string, char_num - 1)

res_1 = 0
res_2 = 0
for j in inp:
    # print(find_next_value_recursive([int(i) for i in j], 12))
    res_1 += int(find_next_value_recursive([int(i) for i in j], 2))
    res_2 += int(find_next_value_recursive([int(i) for i in j], 12))

print("Part One:", res_1)
print("Part Two:", res_2)