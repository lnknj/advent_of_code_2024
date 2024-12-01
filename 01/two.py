left = set()
right = []

with open("./data.txt", "r") as f:
    while line := f.readline():
        line_split = line.rstrip("\n").split("   ")
        left.add(int(line_split[0]))
        right.append(int(line_split[-1]))

similarity = 0
for l in right:
    if l in left:
        similarity += l
        
print(similarity)
