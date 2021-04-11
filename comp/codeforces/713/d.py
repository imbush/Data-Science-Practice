t = int(input())
outs = []
for _ in range(t):
    n = int(input())
    b = sorted(list(map(int, input().split())))
    sum_b = sum(b)
    if 2 * b[-2] == sum_b - b[-1]:
        outs.append(b[:-2])
    else:
        diff = sum_b - 2 * b[-1]
        if diff <= 0:
            outs.append([-1])
        else:
            if diff not in b[:-1]:
                outs.append([-1])
            else:
                b.remove(diff)
                b.append(diff)
                outs.append(b[:-2])
for out in outs:
    print(*out)