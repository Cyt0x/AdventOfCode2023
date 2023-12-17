import sys
import itertools

def readFile():
    with open(sys.path[0] + "\\" + "input.txt") as f:
        return [lines.rstrip("\n") for lines in f.readlines()]

def findEmptyRowCol():
    emptyRows = [i for i, line in enumerate(content) if "#" not in line]
    emptyCols = [j for j, col in enumerate(zip(*content)) if "#" not in col]
    return emptyRows, emptyCols

def findGalaxies():
    galaxies = []
    for row in range(len(content)):
        for col in range(len(content[0])):
            if content[row][col] == "#":
                galaxies.append((row, col))
    return galaxies

def calculateDistances(expansionValue):
    emptyRows, emptyCols = findEmptyRowCol()
    galaxies = findGalaxies()
    distSum = 0
    for (row, col), (nrow, ncol) in itertools.combinations(galaxies, 2):
        dist = abs(nrow - row) + abs(ncol - col)
        for er in emptyRows:
            if min(nrow, row) <= er <= max(nrow, row):
                dist += expansionValue
        for ec in emptyCols:
            if min(ncol, col) <= ec <= max(ncol, col):
                dist += expansionValue
        distSum += dist
    return distSum

content = readFile()
answer1 = calculateDistances(1)
answer2 = calculateDistances(10**6 - 1)

print("Advent of Code 2023 Day 11")
print(f"Result to part 1 is {answer1}")
print(f"Result to part 2 is {answer2}")