import re

input_txt = open("3.txt").read()

REGEX = r"mul\(\d+,\d+\)"

matches = re.findall(REGEX, input_txt)

sum = 0
for match in matches:
    split = match.split(",")
    a = int(split[0][4:])
    b = int(split[1][:-1])
    sum += a * b
print(sum)
