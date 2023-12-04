import sys

def readFile():
    with open(sys.path[0] + "\\" + "input.txt") as f:
        return [lines.rstrip("\n") for lines in f.readlines()]
    
content = readFile()
sumPoints = 0
countCards = [1] * len(content)

for index, line in enumerate(content):
    numParts = line.split(": ")[1].split(" | ")
    winningNums, haveNums = numParts[0].split(), numParts[1].split()
    
    winningCount = len(set(winningNums).intersection(haveNums))
    if winningCount > 0:
        sumPoints += 2 ** (winningCount - 1)
    
    for n in range(winningCount):
        countCards[index + n + 1] += countCards[index]
    

print("Advent of Code 2023 Day 4")

print("Part 1:")
print(sumPoints)

print("\nPart 2:")
print(sum(countCards))