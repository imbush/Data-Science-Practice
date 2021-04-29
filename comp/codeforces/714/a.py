t = int(input())
outs = []
for _ in range(t):
    n, k = list(map(int, input().split()))
    if k > (n - 1) // 2:
        outs.append([-1])
    else:
        outs.append(list(range(1, n + 1)))
        for i in range(k):
            outs[-1][1 + 2 * i], outs[-1][1 + 2 * i + 1] = outs[-1][1 + 2 * i + 1], outs[-1][1 + 2 * i]
for out in outs:
    print(*out)
