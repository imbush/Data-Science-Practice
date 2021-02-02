from math import ceil
t = int(input())
output = []
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    if k < n:
        k = k * ceil(n / k)

    if k % n == 0:
        output.append(k // n)
    else:
        output.append(k // n + 1)
for out in output:
    print(out)