import heapq
from itertools import combinations

# nice but wrong :D (i didn't read the puzzle description correctly)
def puzzle_3_z(filepath):
    joltages = []

    with open(filepath) as f:
        for line in f:
            batteries_indexed = [(idx, int(x)) for idx, x in enumerate(line.strip())]
            top_indices = sorted([idx for idx, x in heapq.nlargest(2, batteries_indexed, key=lambda x: x[1])])
            battery_joltages = [line[x] for x in top_indices]
            joltage = ''.join(battery_joltages)
            joltages.append(int(joltage))

    return sum(joltages)

def puzzle_3(filepath):
    joltages = []

    with open(filepath) as f:
        for line in f:
            line = line.strip()
            batteries = [x for x in line]
            pairs = list(combinations(batteries, 2))
            possible_bank_joltages = [int(''.join(pair)) for pair in pairs]
            max_possible_bank_joltage = max(possible_bank_joltages)
            joltages.append(max_possible_bank_joltage)

    return sum(joltages)



def puzzle_3b(filepath):
    pass



if __name__ == "__main__":
    print("Puzzle 2 - total joltage is:", puzzle_3("2025/resources/puzzle_3.txt"))
    #print("Puzzle 1b - sum of invalid IDs is:", puzzle_3b("2025/resources/puzzle_3.txt"))