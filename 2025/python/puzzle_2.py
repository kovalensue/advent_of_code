def puzzle_2(filepath):

    invalid_ids = []

    with open(filepath) as f:
        for line in f:
            line = line.strip()
            ranges = [x for x in line.split(',')]
            for r in ranges:
                lower_boundary, upper_boundary = r.split('-')[0], r.split('-')[1]
                arr = [str(x) for x in range(int(lower_boundary), int(upper_boundary)+1)]
                for item in arr:
                    if item[:len(item)//2] == item[len(item)//2:]:
                        invalid_ids.append(int(item))

    return sum(invalid_ids)


def puzzle_2b(filepath):
    pass


if __name__ == "__main__":
    print("Puzzle 2 - password is:", puzzle_2("2025/resources/puzzle_2.txt"))
    #print("Puzzle 1b - password is:", puzzle_2b("2025/resources/puzzle_2.txt"))
