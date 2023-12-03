import sys
import re
import math
from collections import defaultdict

def readFile():
    with open(sys.path[0] + "\\" + "input.txt") as f:
        return [lines.rstrip("\n") for lines in f.readlines()]

def findSymbols(input):
    symbols = set()
    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if ((not char.isnumeric()) and (not char == ".")):
                symbols.add((i,j))
    
    return symbols

def matchSymbolsNumbers(input, symbols, symbolNumberDict):
    matchedNumbers = []
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for colIndex, line in enumerate(input):
        for match in re.finditer("\d+", line):
            n = int(match.group(0))            
            numberBorder = set()
            for dr, dc in directions:
                for rowPos in range(match.start(), match.end()):
                    r, c = colIndex + dr, rowPos + dc
                    if 0 <= r < len(input[0]) and 0 <= c < len(input):
                        numberBorder.add((r,c))
            if any(check in numberBorder for check in symbols):
                matchedNumbers.append(n)
            for symbol in symbols.intersection(numberBorder):
                symbolNumberDict[symbol].append(n)

    return matchedNumbers

def sumGearRatio(input, symbolNumberDict):
    gearSum = 0
    for (x,y), numbers in symbolNumberDict.items():
        if input[x][y] == "*" and len(numbers) == 2:
            gearSum += math.prod(numbers)
    return gearSum

content = readFile()
symbolPos = findSymbols(content)
numbersNearSymbol = defaultdict(list)
allMatchingNumbers = matchSymbolsNumbers(content, symbolPos, numbersNearSymbol)

print("Advent of Code 2023 Day 3")

print("Part 1:")
print(sum(allMatchingNumbers))

print("\nPart 2:")
print(sumGearRatio(content, numbersNearSymbol))