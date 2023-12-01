import re

total_sum = 0
with open("input.txt") as f:
        for line in f:
                line = re.sub("\D", "", line)
                if len(line) > 0:
                        total_sum += int(line[0] + line[-1])
print(total_sum)
