t = int(input())
outs = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input()))
    b = list(map(int, input()))
    flips = 0
    a_count = sum(a)
    b_count = sum(b)
    pos = len(a) - 1
    while pos >= 0:
        if (a[pos] + flips) % 2 != b[pos]:
            if a_count == (pos + 1) / 2:
                flips += 1
            else:
                outs.append("NO")
                pos = -1
        if (a[pos] + flips) % 2 == 1:
            a_count -= 1
        pos -= 1
    if pos == -1:
        outs.append("YES")
for out in outs:
    print(out)
