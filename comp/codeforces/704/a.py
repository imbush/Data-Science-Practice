t = int(input())
output = []
for _ in range(t):
    p, a, b, c = [int(x) for x in input().split()]
    if a >= p:
        minimum = a - p
    elif p % a == 0:
        minimum = 0
    else:
        minimum = a - (p % a)
    if b >= p:
        minimum = min(minimum, b - p)
    elif p % b == 0:
        minimum = 0
    else:
        minimum = min(minimum, b - (p % b))
    if c >= p:
        minimum = min(minimum, c - p)
    elif p % c == 0:
        minimum = 0
    else:
        minimum = min(minimum, c - (p % c))
    output.append(minimum)

for out in output:
    print(out)