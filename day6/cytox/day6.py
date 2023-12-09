import sys
import math

def readFile():
    with open(sys.path[0] + "\\" + "input.txt") as f:
         return [lines.rstrip("\n") for lines in f.readlines()]
    
def parse(input):
    time = [int(x) for x in input[0].split(":")[1].split()]
    distance = [int(x) for x in input[1].split(":")[1].split()]
    return time, distance

def waysToWinRace(time, distance):
    minTime = math.ceil((time / 2) - math.sqrt((time / 2) ** 2 - distance))
    maxTime = math.floor((time / 2) + math.sqrt((time / 2) ** 2 - distance))
    return maxTime - minTime + 1

def partOne():
    races = [waysToWinRace(time, distance + 1) for time, distance in zip(timeList, distanceList)]
    return math.prod(races)

def partTwo():
    mergedTime = int("".join(map(str, timeList)))
    mergedDistance = int("".join(map(str, distanceList)))
    return waysToWinRace(mergedTime, mergedDistance + 1)

content = readFile()
timeList, distanceList = parse(content)

print("Advent of Code 2023 Day 6")

print("Part 1:")
print(partOne())

print("\nPart 2:")
print(partTwo())