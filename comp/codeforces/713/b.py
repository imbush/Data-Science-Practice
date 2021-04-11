t = int(input())
outs = []
for _ in range(t):
    n = int(input())
    a = []
    xs = []
    ys = []
    for i in range(n):
        a.append(list(input()))
        if len(xs) < 2:
            for j in range(n):
                if a[i][j] == "*":
                    xs.append(j)
                    ys.append(i)
    if ys[0] == ys[1]:
        if ys[0] == 0:
            a[1][xs[0]] = "*"
            a[1][xs[1]] = "*"
        else:
            a[0][xs[0]] = "*"
            a[0][xs[1]] = "*"
    elif xs[0] == xs[1]:
        if xs[0] == 0:
            a[ys[0]][1] = "*"
            a[ys[1]][1] = "*"
        else:
            a[ys[0]][0] = "*"
            a[ys[1]][0] = "*"
    else:
        a[ys[0]][xs[1]] = "*"
        a[ys[1]][xs[0]] = "*"
    outs.append(a)

for out in outs:
    for line in out:
        print("".join(line))