import itertools

with open("./2024/input/03-06.txt") as f:
    nums = [int(num) for num in f.read().split()]


it = itertools.cycle(".#")
output = []
for num in nums:
    output.append(next(it) * num)

for line in itertools.batched("".join(output), 100):
    print("".join(line))


answer = "4951"
print(answer)
