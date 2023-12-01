import re

def wordtonumber(p_string):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    for i in words:
        p_string = p_string.replace(i, i + str(words.index(i) + 1) + i)
    return p_string

total_sum = 0
with open("input.txt") as f:
        for line in f:
                line = wordtonumber(line)
                line = re.sub("\D", "", line)
                if len(line) > 0:
                        print(line[0] + line[-1])
                        total_sum += int(line[0] + line[-1])
                
print(total_sum)