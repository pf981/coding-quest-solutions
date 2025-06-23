with open("./2024/input/03-08.txt") as f:
    text = f.read()

distance_lines, route_lines = (part.splitlines() for part in text.split("\n\n"))
pois = distance_lines[0].split()

m = {}
for line, poi in zip(distance_lines[1:], pois):
    for d, poi2 in zip(line.split()[1:], pois):
        m[(poi, poi2)] = int(d)

answer = 0
for line in route_lines:
    _, route = line.split(": ")
    route = route.split(" -> ")

    poi = "base"
    for next_poi in route:
        answer += m[(poi, next_poi)]
        poi = next_poi

print(answer)
