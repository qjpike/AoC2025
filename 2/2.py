
def compare_substrings(num, substr_len):
    string = str(num)
    if len(string) % substr_len != 0:
        return 0
        
    substrings = set()
    last_i = 0
    for i in range(substr_len, len(str(num)) + 1, substr_len):
        substrings.add(string[last_i:i])
        last_i = i
    return num if len(substrings) == 1 else 0



with open("input.txt") as f:
    inp = f.read().split(",")

count_1 = 0
count_2 = 0

for i in inp:
    start = int(i.split("-")[0])
    end = int(i.split("-")[1])

    for j in range(start, end + 1):
        for k in range(1, len(str(j))//2 + 1): # this is slow but it works...
            res = compare_substrings(j,k)
            count_2 += res

            if res != 0:
                break
                
        if str(j)[:len(str(j))//2] == str(j)[len(str(j))//2:]:
            count_1 += j

print("Part One:", count_1)
print("Part Two:", count_2) 