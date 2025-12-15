def puzzle_4(filepath):
    paper_rolls_to_remove = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    with open(filepath) as f:
        grid = [list(x.strip()) for x in f.readlines()]
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "@":
                    adjacent = []
                    for dr, dc in directions:
                        new_row, new_col = i + dr, j + dc
                        if (0 <= new_row <= len(grid) - 1) and (0 <= new_col <= len(grid[0]) - 1):
                            adjacent.append(grid[new_row][new_col])
                    if adjacent.count("@") < 4:
                        paper_rolls_to_remove.append((i, j))

        return len(paper_rolls_to_remove)


def remove_rolls(grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    rolls_removed = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                adjacent = []
                for dr, dc in directions:
                    new_row, new_col = i + dr, j + dc
                    if (0 <= new_row <= len(grid) - 1) and (0 <= new_col <= len(grid[0]) - 1):
                        adjacent.append(grid[new_row][new_col])
                if adjacent.count("@") < 4:
                    grid[i][j] = "."
                    rolls_removed += 1

    if rolls_removed == 0:
        return 0

    return rolls_removed + remove_rolls(grid)


def puzzle_4b(filepath):
    with open(filepath) as f:
        grid = [list(x.strip()) for x in f.readlines()]
        return remove_rolls(grid)


if __name__ == "__main__":
    print("Puzzle 4 - number of valid paper rolls to move:", puzzle_4("2025/resources/puzzle_4.txt"))
    print("Puzzle 4 - total number of removed rolls:", puzzle_4b("2025/resources/puzzle_4.txt"))
