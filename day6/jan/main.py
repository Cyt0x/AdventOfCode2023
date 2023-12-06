from typing import List
from math import ceil, floor, sqrt
import re

import time
start_time = time.time()

data = open("example.txt").readlines()
#data = open("input.txt").readlines()

lines = []

for line in data:
    lines.append(line.rstrip("\n"))

def ints(s:str) -> List[int]:
    list_as_str = re.findall(r'([-+]?\d+)', s)
    return list(map(int, list_as_str))

times = ints(lines[0])
distances = ints(lines[1])

def race(time, distance):
    minimal_time = (time - sqrt(time ** 2 - 4 * distance)) / 2
    maximal_time = (time + sqrt(time ** 2 - 4 * distance)) / 2
    return ceil(maximal_time - 1) - floor(minimal_time + 1) + 1

product = 1
for i in range(len(times)):
    product *= race(times[i], distances[i])
    
print(f"Part 1: {product}")

time_two = int(lines[0].split(":")[1].replace(" ", ""))
distance = int(lines[1].split(":")[1].replace(" ", ""))

print(f"Part 2: {race(time_two, distance)}")


print("--- %s seconds ---" % (time.time() - start_time))
