input_txt = open("2.txt").read()

safe_count = 0

for line in input_txt.splitlines():
    levels = [int(v) for v in line.split()]
    length = len(levels)
    if levels[0] - levels[1] > 0:
        levels = list(reversed(levels))
    if levels != sorted(levels):
        continue
    diffs = []
    for i in range(0, length - 1):
        diffs.append(levels[i + 1] - levels[i])
    if max(diffs) > 3 or min(diffs) == 0:
        continue
    print(f"{levels} is safe")
    safe_count += 1

print(safe_count)
