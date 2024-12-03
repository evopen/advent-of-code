input_txt = open("2.txt").read()

safe_count = 0


def is_valid(levels: list[int]):
    length = len(levels)
    if levels[0] - levels[1] > 0:
        levels = list(reversed(levels))
    diffs = []
    for i in range(0, length - 1):
        diffs.append(levels[i + 1] - levels[i])
    for diff in diffs:
        if diff > 3 or diff <= 0:
            return False
    return True


for line in input_txt.splitlines():
    levels = [int(v) for v in line.split()]
    length = len(levels)
    if is_valid(levels):
        safe_count += 1
        continue
    # remove one level
    for i in range(length):
        new_levels = levels[:i] + levels[i + 1 :]
        if not is_valid(new_levels):
            continue
        safe_count += 1
        break


print(safe_count)
