import re

def puzzle_3(filepath):
    line_numbers = []
    line_symbols = []
    part_numbers = []

    with open(filepath) as f:

        def match_symbol(start, end, symbols):
            for s in symbols:
                if s >= start - 1 and s <= end + 1:
                    return True
            return False

        for line in f:
            line = line.strip()

            # exit when no more line to process
            if not line:
                break

            # find all numbers in given line
            numbers = [(n.group(), int(n.start()), int(n.end())) for n in re.finditer("[0-9]+", line)]
            line_numbers.append(numbers)

            # find all symbols in given line
            symbols = [i for i, char in enumerate(line) if char not in ".0123456789"]
            line_symbols.append(symbols)

        for i, n in enumerate(line_numbers):
            for num, start, end in n:
                is_match = match_symbol(start, end, line_symbols[i])
                if i > 0:
                    is_match = is_match or match_symbol(start, end, line_symbols[i - 1])
                if i < len(line_numbers) - 1:
                    is_match = is_match or match_symbol(start, end, line_symbols[i + 1])
                if is_match:
                    part_numbers.append(int(num))

        return sum(part_numbers)

def puzzle_3_refactored(filepath):
    part_numbers = []

    with open(filepath) as f:
        lines = [line.strip() for line in f.readlines()]
        for i, line in enumerate(lines):
            for match in re.finditer(r"\d+", line):
                num = int(match.group())
                start = match.start()
                end = match.end()-1

                is_part = False

                for r in range(max(0, i-1), min(len(lines), i+2)):
                    for c in range(max(0, start-1), min(len(lines[r]), end+2)):
                        char = lines[r][c]
                        if char not in '.1234567890':
                            is_part = True
                            break
                    if is_part:
                        break

                if is_part:
                    part_numbers.append(num)

    return sum(part_numbers)


def puzzle_3b(filepath):
    pass


if __name__ == "__main__":
    #print(puzzle_3("/home/kovalikt/git/personal/advent_of_code/resources/puzzle_3.txt"))
    print(puzzle_3_refactored("/home/kovalikt/git/personal/advent_of_code/resources/puzzle_3.txt")) # 539590
    #print(puzzle_3b("/home/kovalikt/git/personal/advent_of_code/resources/puzzle_3.txt"))
