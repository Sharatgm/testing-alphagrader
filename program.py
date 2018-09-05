#Just realized that pushing added a new submission

import fileinput

lines = []

for line in fileinput.input():
    lines.append(int(line))

print(sum(lines))
