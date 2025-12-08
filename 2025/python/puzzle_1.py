
from hmac import new


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

    pos = 50
    psw = 0

    with open(file_path) as f:
        for line in f:
            line = line.strip()
            print(pos%100, pos, )
            if line.startswith("R"):
                pos = pos + int(line[1:])
            elif line.startswith("L"):
                pos = pos - int(line[1:])


            if (pos%100)-pos == 100:
                psw += 1

    return psw


if __name__ == "__main__":
    print("Puzzle 1 - password is:", puzzle_1("2025/resources/puzzle_1.txt"))
    print("Puzzle 1b - password is:", puzzle_1b("2025/resources/puzzle_1_test.txt"))