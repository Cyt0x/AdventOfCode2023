from typing import List
import re

import time
start_time = time.time()

#data = open("example.txt").readlines()
data = open("input.txt").readlines()

lines = []

for line in data:
    lines.append(line.rstrip("\n"))

def ints(s:str) -> List[int]:
    list_as_str = re.findall(r'([-+]?\d+)', s)
    return list(map(int, list_as_str))

times = ints(lines[0])
distances = ints(lines[1])

def race(time, distance):
    num = 0
    for speed in range(1, time):
        time_left = time - speed
        if time_left * speed > distance:
            num +=1
    return num
    
product = 1
for i in range(len(times)):
    product *= race(times[i], distances[i])
    
print(f"Part 1: {product}")

times = int(lines[0].split(":")[1].replace(" ", ""))
distance = int(lines[1].split(":")[1].replace(" ", ""))

print(f"Part 2: {race(times, distance)}")


print("--- %s seconds ---" % (time.time() - start_time))
