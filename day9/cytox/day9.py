import sys

def readFile():
    with open(sys.path[0] + "\\" + "input.txt") as f:
         return [lines.rstrip("\n") for lines in f.readlines()]
  
def predictNext(line):
    lines = [line]
    while (not all(val == 0 for val in lines[-1])):
        lines.append([b - a for a, b in (zip(lines[-1], lines[-1][1:]))])
    return sum([line[-1] for line in lines])    

content = [[int(val) for val in line.split()] for line in readFile()]

answer1 = sum([predictNext(line) for line in content])
answer2 = sum([predictNext(line[::-1]) for line in content])

print("Advent of Code 2023 Day 9")
print(f"Result to part 1 is {answer1}")
print(f"Result to part 2 is {answer2}")