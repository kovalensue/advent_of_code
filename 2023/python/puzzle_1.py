# Link to puzzle: https://adventofcode.com/2023/day/1
import re


def puzzle_1(filepath: str) -> int:
    calibration_numbers = []

    with open(filepath) as f:
        for line in f:
            numbers = re.findall("[0-9]{1}", line)
            calibration_numbers.append(int(str(numbers[0]) + str(numbers[-1])))

    return sum(calibration_numbers)


def puzzle_1b(filepath: str) -> int:
    calibration_numbers = []
    digit_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }
    regexp = "(?=([0-9]|zero|one|two|three|four|five|six|seven|eight|nine){1})"

    with open(filepath) as f:
        for line in f:
            numbers = re.findall(regexp, line)
            calibration_numbers.append(int(digit_dict[numbers[0]] + digit_dict[numbers[-1]]))

    return sum(calibration_numbers)


if __name__ == "__main__":
    print(puzzle_1("/home/kovalikt/git/personal/advent_of_code/resources/puzzle_1.txt"))  # 53080
    print(puzzle_1b("/home/kovalikt/git/personal/advent_of_code/resources/puzzle_1.txt"))  # 53268
