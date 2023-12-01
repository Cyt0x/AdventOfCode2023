import sys
import re

def readFile():
    with open(sys.path[0] + "\\" + "input.txt") as f:
        return [lines.rstrip("\n") for lines in f.readlines()]

def sumCalibration(content):
    onlyNumbers = [re.findall("\d", c) for c in content]
    return sum(int(line[0] + line[-1]) for line in onlyNumbers)

def addTextNumbers(content):
    for index, value in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        content = [line.replace(value, value + str(index + 1) + value) for line in content]
    return content

print("Advent of Code 2023 Day 1")
content = readFile()

print("Part 1:")
print(sumCalibration(content))

print("\nPart 2:")
print(sumCalibration(addTextNumbers(content)))