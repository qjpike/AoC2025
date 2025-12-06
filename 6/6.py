with open("input.txt") as f:
    inp = [i.strip().split() for i in f.readlines()]

with open("input.txt") as f:
    inp_2 = [i[:-1] for i in f.readlines()]

count_1 = 0
for i, operand in enumerate(inp[-1]):
    if operand == "+":
        count_1 += int(inp[0][i]) + int(inp[1][i]) + int(inp[2][i]) + int(inp[3][i])
    elif operand == "*":
        count_1 += int(inp[0][i]) * int(inp[1][i]) * int(inp[2][i]) * int(inp[3][i])

print(count_1) 

count_2 = 0
idx = 0
while idx <= len(inp_2[-1]):
    operand = inp_2[-1][idx]
    
    if "*" not in inp_2[-1][idx+1:]:
        mul_idx = 100000000000
    else:
        mul_idx = inp_2[-1][idx+1:].index("*")

    if "+" not in inp_2[-1][idx+1:]:
        plus_idx = 100000000000
    else:
        plus_idx = inp_2[-1][idx+1:].index("+")

    if mul_idx == plus_idx == 100000000000:
        next_idx = len(inp_2[-1]) + idx + 1
    else:
        next_idx = min(mul_idx, plus_idx) + idx

    row_0 = inp_2[0][idx:next_idx]
    row_1 = inp_2[1][idx:next_idx]
    row_2 = inp_2[2][idx:next_idx]
    row_3 = inp_2[3][idx:next_idx]

    col_amount = 1 if operand == "*" else 0
    for i in range(len(row_0)-1, -1, -1):
        if operand == "*":
            col_amount *= int(row_0[i] + row_1[i] + row_2[i] + row_3[i])
        else:
            col_amount += int(row_0[i] + row_1[i] + row_2[i] + row_3[i])

    count_2 += col_amount 
    idx = next_idx + 1

print(count_2)