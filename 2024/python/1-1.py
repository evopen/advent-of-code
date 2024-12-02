input_list = open("1.txt").read()
left  = []
right = []
for line in input_list.splitlines():
    split = line.split(maxsplit=1)
    left.append(int(split[0].strip()))
    right.append(int(split[1].strip()))


left = sorted(left)
right = sorted(right)


dist = 0
for i in range(len(left)):
    dist += abs(left[i] - right[i])

print("Distance: ", dist)