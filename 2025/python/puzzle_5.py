def puzzle_5(filepath):
    fresh_ids = set()

    with open(filepath) as f:
        ranges = []
        ids = []

        for line in f:
            line = line.strip()
            if len(line.split("-")) == 2:
                ranges.append(line)
            elif len(line.split("-")) != 2 and len(line.strip()) > 0:
                ids.append(line)

        for id in ids:
            for range in ranges:
                lower, upper = tuple(range.split("-"))
                if int(lower) <= int(id) <= int(upper):
                    fresh_ids.add(int(id))

    return len(fresh_ids)


def puzzle_5b(filepath):
    ranges = []

    number_of_fresh_ids = 0

    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if len(line.split("-")) == 2:
                ranges.append(tuple(map(int, line.split("-"))))

        ranges_sorted = sorted(ranges, key=lambda x: x[0])

        no_overlaps = []

        previous_start, previous_end = ranges_sorted[0]
        for start, end in ranges_sorted[1:]:
            if start <= previous_end:
                previous_end = max(previous_end, end)
            else:
                no_overlaps.append((previous_start, previous_end))
                previous_start, previous_end = start, end

        no_overlaps.append((previous_start, previous_end))

        for start, end in no_overlaps:
            number_of_fresh_ids = number_of_fresh_ids + (end - start) + 1

        return number_of_fresh_ids


if __name__ == "__main__":
    print("Puzzle 5 - number of fresh IDs:", puzzle_5("2025/resources/puzzle_5.txt"))
    print("Puzzle 5 - possible number of fresh ingredients:", puzzle_5b("2025/resources/puzzle_5.txt"))
