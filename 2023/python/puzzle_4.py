from regex import P


def puzzle_4(filepath):
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            numbers = line.split(":")[1].strip()
            print(numbers)

    return "TBD"


def puzzle_4b(filepath):
    pass


if __name__ == "__main__":
    print(puzzle_4("./resources/puzzle_4.txt"))
    print(puzzle_4b("./resources/puzzle_4.txt"))
