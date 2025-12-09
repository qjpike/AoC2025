def merge_intersections(list_of_sets):
    for j in range(len(list_of_sets)):
        merge = True
        while merge:
            merge = False
            new_list = []
            merged = list_of_sets[0]
            for i in list_of_sets[1:]:
                if len(merged.intersection(i)) != 0:
                    merged = merged.union(i)
                    merge = True
                else:
                    new_list.append(i)

            list_of_sets = new_list
            list_of_sets.append(merged)

    return list_of_sets

with open("input.txt") as f:
    jb_list = [(int(i.split(",")[0]), int(i.split(",")[1]), int(i.split(",")[2].strip())) for i in f.readlines()]

dist_list = []
for i, start_jb in enumerate(jb_list):
    for end_jb in jb_list[i+1:]:
        # if start_jb == end_jb:
        #     continue
        # else:
        dist_list.append( ((start_jb[0] - end_jb[0])**2 + (start_jb[1] - end_jb[1])**2 + (start_jb[2] - end_jb[2])**2, start_jb, end_jb) )

dist_list.sort()

max_list = 0
circuit_list = []
for start_jb in range(len(dist_list)):
    circuit_list.append({dist_list[start_jb][1],dist_list[start_jb][2]})
    circuit_list = merge_intersections(circuit_list)
    if start_jb == 999:
        circuit_counts = [len(i) for i in circuit_list]
        circuit_counts.sort(reverse=True)
        print("Part One:", circuit_counts[0] * circuit_counts[1] * circuit_counts[2])

    if len(circuit_list) == 1 and len(circuit_list[0]) == len(jb_list):
        print("Part Two:", dist_list[start_jb][1][0] * dist_list[start_jb][2][0])     
        break
