import itertools
import string

with open("./2024/input/03-11.txt") as f:
    text = f.read()

_, key, _, message = text.splitlines()
key = key.split(": ")[1]
message = message.split(": ")[1]

grid = []
for c in key + string.ascii_lowercase:
    if c == "j":
        c = "i"
    if c not in grid:
        grid.append(c)

grid = list(itertools.batched(grid, 5))
m = {}
for r in range(len(grid)):
    for c in range(len(grid[0])):
        m[grid[r][c]] = (r, c)

answer = []
for word in message.split():
    assert len(word) % 2 == 0

    decoded = []
    for a, b in itertools.batched(word, 2):
        assert a != b
        assert a != "j"
        assert b != "j"

        r1, c1 = m[a]
        r2, c2 = m[b]

        if r1 == r2:
            decoded.append(grid[r1][c1 - 1])
            decoded.append(grid[r2][c2 - 1])
            continue
        if c1 == c2:
            decoded.append(grid[r1 - 1][c1])
            decoded.append(grid[r2 - 1][c2])
            continue

        decoded.append(grid[r1][c2])
        decoded.append(grid[r2][c1])

    answer.append("".join(decoded))

answer = " ".join(answer)
print(answer)
