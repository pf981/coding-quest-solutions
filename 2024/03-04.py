import collections

with open("./2024/input/03-04.txt") as f:
    lines = f.read().splitlines()

prices = collections.defaultdict(int)
for line in lines:
    name, fee_type, price = line.split()
    name = name[:-1]
    price = int(price)

    assert fee_type in ["Seat", "Meals", "Luggage", "Fee", "Tax", "Discount", "Rebate"]
    if fee_type in ["Discount", "Rebate"]:
        price = -price

    prices[name] += price

answer = min(prices.values())
print(answer)
