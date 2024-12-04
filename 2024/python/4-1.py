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
        if grid[y][x] != "X":
            continue
        # east
        if x + 3 < width and grid[y][x : x + 4] == WORD:
            count += 1
        # south-east
        if (
            x + 3 < width
            and y + 3 < height
            and [grid[y + i][x + i] for i in range(4)] == WORD
        ):
            count += 1
        # south
        if y + 3 < height and [grid[y + i][x] for i in range(4)] == WORD:
            count += 1
        # south-west
        if (
            x - 3 >= 0
            and y + 3 < height
            and [grid[y + i][x - i] for i in range(4)] == WORD
        ):
            count += 1
        # west
        if x - 3 >= 0 and [grid[y][x - i] for i in range(4)] == WORD:
            count += 1
        # north-west
        if x - 3 >= 0 and y - 3 >= 0 and [grid[y - i][x - i] for i in range(4)] == WORD:
            count += 1
        # north
        if y - 3 >= 0 and [grid[y - i][x] for i in range(4)] == WORD:
            count += 1
        # north-east
        if (
            x + 3 < width
            and y - 3 >= 0
            and [grid[y - i][x + i] for i in range(4)] == WORD
        ):
            count += 1


print(count)
