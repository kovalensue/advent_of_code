def puzzle_2(filepath):
    max_allowed_count = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    idx = 0
    possible_games = []

    with open(filepath) as f:
        for line in f:
            is_possible = True
            idx += 1
            game_data = line.split(": ")
            game_id = int(game_data[0].split(" ")[-1])
            hands = game_data[1].strip().split("; ")

            for h in hands:
                cubes = h.split(", ")
                for c in cubes:
                    key = c.split(" ")[-1]
                    val = c.split(" ")[0]
                    if int(val) > max_allowed_count[key]:
                        is_possible = False
                        break

            if is_possible:
                possible_games.append(game_id)

    return sum(possible_games)


def puzzle_2b(filepath):
    power_all_games = []

    with open(filepath) as f:
        for line in f:
            game_data = line.split(": ")
            hands = game_data[1].strip().split("; ")

            max_dict = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }

            for h in hands:
                cubes = h.split(", ")
                for c in cubes:
                    key = c.split(" ")[-1]
                    val = c.split(" ")[0]
                    if int(val) > max_dict[key]:
                        max_dict[key] = int(val)

            power_all_games.append(max_dict["red"] * max_dict["green"] * max_dict["blue"])

    return sum(power_all_games)


if __name__ == "__main__":
    print(puzzle_2("/home/kovalikt/git/personal/advent_of_code/resources/puzzle_2.txt")) # 2176
    print(puzzle_2b("/home/kovalikt/git/personal/advent_of_code/resources/puzzle_2.txt")) # 63700
