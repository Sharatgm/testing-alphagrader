import fileinput

lines = []

for line in fileinput.input():
    lines.append(int(line))

print(sum(lines))
