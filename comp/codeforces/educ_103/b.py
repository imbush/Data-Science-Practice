from math import ceil

t = int(input())
output = []
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    ps = [int(p) for p in input().split()]
    max_diff = 0
    count = ps[0]
    for i in range(1, n):
        p_diff = ceil((100 * ps[i]) / k) - count
        max_diff = max(p_diff, max_diff)
        count += ps[i]
    output.append(max_diff)

for out in output:
    print(out)