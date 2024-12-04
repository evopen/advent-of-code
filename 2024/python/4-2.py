from collections import Counter


input_txt = open("4.txt").read()

lines = input_txt.splitlines()

grid: list[list[str]] = []


for line in lines:
    row = []
    for char in line:
        row.append(char)
    grid.append(row)

width = len(grid[0])
height = len(grid)

print(f"Width: {width}, Height: {height}")


count = 0

WORD = ["X", "M", "A", "S"]


for y in range(height):
    for x in range(width):
        if grid[y][x] != "A":
            continue
        if x + 1 < width and x - 1 >= 0 and y + 1 < height and y - 1 >= 0:
            counter1 = Counter()
            counter1[grid[y + 1][x + 1]] += 1
            counter1[grid[y - 1][x - 1]] += 1
            counter2 = Counter()
            counter2[grid[y + 1][x - 1]] += 1
            counter2[grid[y - 1][x + 1]] += 1
            if (
                counter1["M"] == 1
                and counter1["S"] == 1
                and counter2["M"] == 1
                and counter2["S"] == 1
            ):
                count += 1


print(count)
