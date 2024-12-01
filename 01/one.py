left = []
right = []

with open("./data.txt", "r") as f:
    while line := f.readline():
        line_split = line.rstrip("\n").split("   ")
        left.append(int(line_split[0]))
        right.append(int(line_split[-1]))

sorted_left = sorted(left)
sorted_right = sorted(right)

total_distance = 0
for i, _ in enumerate(sorted_left):
    total_distance += abs(sorted_left[i] - sorted_right[i])
print(total_distance)
