import downloader

text = downloader.get_puzzle(17).strip()

lookup = """A 0010
E 0000
T 0001
I 0011
N 0100
O 0101
S 0110
H 0111
R 10000
D 10001
L 10010
U 10011
C 10100
M 10101
F 10110
B 10111
F 1100000
Y 1100001
W 1100010
G 1100011
P 1100100
B 1100101
V 1100110
K 1100111
Q 1101000
J 1101001
X 1101010
Z 1101011
0 1110000
1 1110001
2 1110010
3 1110011
4 1110100
5 1110101
6 1110110
7 1110111
8 1111000
9 1111001
_ 1111010
. 1111011
' 1111100
* 1111111"""

m = {}
for line in lookup.splitlines():
    a, b = line.split()
    m[int(b, 2)] = a

encoded = [int(c == "1") for c in bin(int(text, 16))[2:]]
encoded.reverse()

message = []
i = 0
while encoded:
    num = 0
    for _ in range(4):
        num <<= 1
        num |= encoded.pop()
    while num not in m:
        num <<= 1
        num |= encoded.pop()

    if m[num] == "*":
        break
    message.append(m[num])

print("".join(message))

answer = 42 * 42
print(answer)
