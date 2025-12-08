def puzzle_1(file_path):
    pos = 50
    psw = 0

    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if line.startswith("R"):
                pos = pos + int(line[1:])
            elif line.startswith("L"):
                pos = pos - int(line[1:])
            if pos % 100 == 0:
                psw += 1
    return psw


def puzzle_1b(file_path):
    N = 100
    pos = 50
    wraps = 0

    with open(file_path) as f:
        for line in f:
            line = line.strip()
            old_pos = pos
            if line.startswith("R"):
                pos = pos + int(line[1:])
                arr = [(x+1)%N for x in list(range(old_pos, pos, 1))]
            elif line.startswith("L"):
                pos = pos - int(line[1:])
                arr = [(x-1)%N for x in list(range(old_pos, pos, -1))]

            wraps += arr.count(0)

    return wraps


if __name__ == "__main__":
    print("Puzzle 1 - password is:", puzzle_1("2025/resources/puzzle_1.txt"))
    print("Puzzle 1b - password is:", puzzle_1b("2025/resources/puzzle_1.txt"))
