with open('input.txt') as file:
    joltage = [int(x) for x in file.read().splitlines()]

diff1 = 0
diff3 = 1

joltage.sort()

difference = joltage[0]
if difference == 1:
    diff1 += 1
if difference == 3:
    diff3 += 1

for i in range(1, len(joltage)):
    difference = joltage[i] - joltage[i-1]
    if difference == 1:
        diff1 += 1
    if difference == 3:
        diff3 += 1

print(diff1 * diff3)
