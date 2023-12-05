def read_input(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def parse_blocks(data):
    return data.split('\n\n')

def extract_seeds_and_inputs(blocks):
    seeds, *inputs = blocks
    seeds = [int(x) for x in seeds.split(':')[1].split()]
    return seeds, inputs

class Function:
    def __init__(self, string):
        lines = string.split('\n')[1:]
        self.tuples = [[int(x) for x in line.split()] for line in lines]

    def part_one(self, i):
        for (destination, source, size) in self.tuples:
            if source <= i < source + size:
                return i + destination - source
        return i

    def part_two(self, ranges):
        hit = []
        for (destination, source, size) in self.tuples:
            src_end = source + size
            new_range = []
            while ranges:
                (start, end) = ranges.pop()
                before = (start, min(end,source))
                interval = (max(start, source), min(src_end, end))
                after = (max(src_end, start), end)
                if before[1] > before[0]:
                    new_range.append(before)
                if interval[1] > interval[0]:
                    hit.append((interval[0] - source + destination, interval[1] - source + destination))
                if after[1] > after[0]:
                    new_range.append(after)
            ranges = new_range
        return hit + ranges

def get_function_instances(blocks):
    return [Function(block) for block in blocks]

def solve_part_one(seeds, functions):
    p1_solution = []
    for x in seeds:
        for f in functions:
            x = f.part_one(x)
        p1_solution.append(x)
    return min(p1_solution)

def solve_part_two(seeds, functions):
    p2_solution = []
    # All even seeds and all odd seeds paired
    pairs = list(zip(seeds[::2], seeds[1::2]))
    for start, size in pairs:
        ranges = [(start, start + size)]
        for f in functions:
            ranges = f.part_two(ranges)
        p2_solution.append(min(ranges)[0])
    return min(p2_solution)

# Read input file
#input_data = read_input("example.txt")
input_data = read_input("input.txt")
input_blocks = parse_blocks(input_data)

seeds, inputs = extract_seeds_and_inputs(input_blocks)
function_instances = get_function_instances(input_blocks)

solution_part_one = solve_part_one(seeds, function_instances)
print(solution_part_one)

solution_part_two = solve_part_two(seeds, function_instances)
print(solution_part_two)
