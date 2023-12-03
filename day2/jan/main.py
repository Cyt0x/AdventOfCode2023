import re

#data = open("example.txt").readlines()
data = open("input.txt").readlines()

r = 12
g = 13
b = 14
sum = 0
p2_power = 0

for line in data:
    line = line.strip("\n")
    split = line.split(":")
    game = int(re.sub("\D", "", split[0]))
    game_summary = split[1]
    max_red = max_blue = max_green = 0
    pulls = game_summary.split(";")
    for pull in pulls:
        single_color_pull = pull.split(",")
        for color in single_color_pull:
            number_pulled = int(re.sub("\D", "", color))
            if "red" in color and number_pulled > max_red:
                max_red = number_pulled
            elif "blue" in color and number_pulled > max_blue:
                max_blue = number_pulled
            elif "green" in color and number_pulled > max_green:
                max_green = number_pulled
    if max_red <= r and max_green <= g and max_blue <= b:
        sum += game
    p2_power += max_red * max_blue * max_green
print(f"Part 1 sum is: {sum}")
print(f"Part 2 power is: {p2_power}")
