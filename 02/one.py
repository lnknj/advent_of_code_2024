with open("./data.txt", "r") as f:
    lines = f.readlines()

unsafe_lines = 0
for l in lines:
    p = l.rstrip("\n").split(" ")
    if int(p[0]) < int(p[1]):
        line_should_decrease = False
    elif int(p[0]) > int(p[1]):
        line_should_decrease = True
    else:
        unsafe_lines += 1
        continue

    for i, _ in enumerate(p):
        if i+1 >= len(p):
            break
        if (abs(int(p[i+1]) - int(p[i])) > 3) or (abs(int(p[i+1]) - int(p[i])) < 1):
            unsafe_lines += 1
            break
        if (int(p[i+1]) > int(p[i])) == line_should_decrease:
            unsafe_lines += 1
            break
            
print(len(lines) - unsafe_lines)