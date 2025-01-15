import re

with open("Lists/data4.txt") as  file:
    reports = file.read().split("\n")
    reports = [report.split() for report in reports]
    reports = [[str(string) for string in report] for report in reports]

print(reports)

def count_how_many(grid, word = "XMAS"):
    word_length = len(word)
    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (0,1), (1,0), (1, 1), (-1,1),
        (0, -1), (-1, 0), (-1, -1), (1, -1)
    ]

    count = 0
    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if all(0 <= r + i * dx < rows and 0 <= c + i * dy < cols and grid[r + i * dx][c + i * dy] == word[i] for i in range(word_length)):
                    count += 1
    return count
data = [
    ["MMMSXXMASM"],
    ["MSAMXMSMSA"],
    ["AMXSXMAAMM"],
    ["MSAMASMSMX"],
    ["XMASAMXAMM"],
    ["XXAMMXXAMA"],
    ["SMSMSASXSS"],
    ["SAXAMASAAA"],
    ["MAMMMXMMMM"],
    ["MXMXAXMASX"]
]


process_data = [row[0] for row in reports]
print(count_how_many(process_data))