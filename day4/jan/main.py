#data = open("example.txt").readlines()
data = open("input.txt").readlines()
sum = 0

for line in data:
    line = line.strip("\n")
    card_numbers = line.split(" | ")[0].split(": ")[1].split(" ")
    card_numbers[:] = [int(x) for x in card_numbers if x]
    winning_numbers = line.split(" | ")[1].split(" ")
    winning_numbers = [int(x) for x in winning_numbers if x]
    matches_card = 0    
    for number in card_numbers:
        if number in winning_numbers:
            matches_card +=1
    if matches_card > 0:
        sum += 2**(matches_card-1)

print(f"Score is: {sum}")
