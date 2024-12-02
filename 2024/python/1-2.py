from collections import Counter


input_list = open("1.txt").read()
left  = []
right = Counter()
for line in input_list.splitlines():
    split = line.split(maxsplit=1)
    left_num = int(split[0].strip())
    right_num = int(split[1].strip())
    left.append(left_num)
    right[right_num] += 1



score = 0
for i in range(len(left)):
    score += left[i] * right[left[i]]

print("Score: ", score)