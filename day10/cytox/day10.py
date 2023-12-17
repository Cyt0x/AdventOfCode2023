import sys
from collections import deque
from matplotlib import Path

def readFile():
    with open(sys.path[0] + "\\" + "input.txt") as f:
        return [lines.rstrip("\n") for lines in f.readlines()]

def findStart():
    for y, line in enumerate(content):
        for x, tile in enumerate(line):
            if tile == "S":
                return x,y

def getNeighborsQueue():
    x,y = startX, startY
    q = deque()
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        symbol = content[x + dx][y + dy]
        if symbol in pipeSymbols:
            for nx, ny in pipeSymbols[symbol]:
                if (x == (x + dx + nx)) and (y == (y + dy + ny)):
                    q.append(((x + dx, y + dy), 1))
    return q

def calcDistances(q):
    dists = {(startX, startY) : 0}
    while q:
        (nx, ny), dist = q.popleft()
        if (nx,ny) in dists:
            continue
        dists[(nx,ny)] = dist

        for dy, dx in pipeSymbols[content[ny][nx]]:
            q.append(((nx+dx, ny+dy), dist+1))
    return dists

def calculateLoopArea(loop):
    loop = []
    for index, x in enumerate(loop):
        if index % 2 == 0:
            loop.insert(0,x)
        else:
            loop.append(list(x))
    x, y = zip(*loop)
    return 0.5 * abs(sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(loop))))

def partTwo():
    border = calcDistances(getNeighborsQueue())
    area = calculateLoopArea(border)
    return int(area - 0.5 * len(border) + 1)

content = readFile()
pipeSymbols = {
        "|" : [(-1, 0), (1, 0)],
        "-" : [(0, -1), (0, 1)],
        "L" : [(-1, 0), (0, 1)],
        "J" : [(0, -1), (-1, 0)],
        "7" : [(1, 0), (0, -1)],
        "F" : [(1, 0), (0, 1)]
        }
startX, startY = findStart()   

answer1 = max(calcDistances(getNeighborsQueue()).values())
answer2 = partTwo()

print("Advent of Code 2023 Day 10")
print(f"Result to part 1 is {answer1}")
print(f"Result to part 2 is {answer2}")