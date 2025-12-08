from math import floor


def puzzle_4(filepath):
    """
    Calculate the points for each card based on the winning and played numbers.
    The points are calculated as 2^(n-1) where n is the number of matches.
    """
    points = []

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            numbers = line.split(":")[1].strip().split("|")
            winning_numbers = set([int(x) for x in numbers[0].strip().split(" ") if x])
            played_numbers = set([int(x) for x in numbers[1].strip().split(" ") if x])
            match_cnt = len(played_numbers.intersection(winning_numbers))
            points.append(floor(pow(2, match_cnt - 1)))

    return sum(points)


def puzzle_4b(filepath):
    pass


if __name__ == "__main__":
    print(puzzle_4("./resources/puzzle_4.txt"))  # 21213
    print(puzzle_4b("./resources/puzzle_4.txt"))
