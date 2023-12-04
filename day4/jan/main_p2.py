#data = open("example.txt").readlines()
data = open("input.txt").readlines()
sum = len(data)

def process_line(line_index, data):
    line = data[line_index].strip("\n")
    card_numbers = line.split(" | ")[0].split(": ")[1].split(" ")
    card_numbers[:] = [int(x) for x in card_numbers if x]
    winning_numbers = line.split(" | ")[1].split(" ")
    winning_numbers = [int(x) for x in winning_numbers if x]
    matches_card = 0    
    for number in card_numbers:
        if number in winning_numbers:
            matches_card +=1
    if matches_card > 0:
        for i in range(1, matches_card+1):
            matches_card += process_line(line_index + i, data)
    return matches_card


for line_index in range(len(data)):
    print(f"Current sum after Card {line_index + 1} is {sum}")
    sum += process_line(line_index, data)
    

print(f"Score is: {sum}")
