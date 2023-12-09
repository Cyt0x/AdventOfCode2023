import sys

def readFile():
    with open(sys.path[0] + "\\" + "test.txt") as f:
        return f.read().strip()

def parseInput(input):
    blocks = input.split("\n\n")
    
    seeds = list([int(x) for x in blocks[0].split()[1:]])

    tuples = []
    for maps in blocks[1:]:
        tuples.append([[int(x) for x in line.split()] for line in maps.split("\n")[1:]])
    
    return seeds, tuples

def applyMapping(seed):
    for maps in tuples:
        for toNum, fromNum, rangeLen in maps:
            if fromNum <= seed < fromNum + rangeLen:
                seed = toNum + (seed - fromNum)
                break
    return seed

def applyReverseMapping(seed):
    for maps in tuples:
        for fromNum, toNum, rangeLen in maps:
            if fromNum <= seed < fromNum + rangeLen:
                seed = toNum + (seed - fromNum)
                break
    return seed

def iamstupid():
    tuples.reverse()
    for i in range(0, sys.maxsize):
        val = applyReverseMapping(i)
        for seedIndex in range(0, len(seeds)-1,2):
            if seeds[seedIndex] <= val < (seeds[seedIndex] + seeds[seedIndex + 1] - 1):
                return i

content = readFile()
seeds, tuples = parseInput(content)

print("Advent of Code 2023 Day 5")

print("Part 1:")
print(min([applyMapping(seed) for seed in seeds]))

print("\nPart 2:")
print(iamstupid())