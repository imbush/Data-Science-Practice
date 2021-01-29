t = int(input())
output = []
for i in range(t):
    two_n = 2 * int(input())
    ds = sorted([int(d) for d in input().split()])
    pairs = True
    for i in range(0, len(ds), 2):
        if ds[i] != ds[i + 1]:
            pairs = False
            output.append("NO")
            break

    if pairs:
        yes = True
        last = -1
        for i in range(two_n, 0, -2):
            d = ds.pop()
            diff = 2 * ds.pop() // i
            if d % i == 0 and d != 0 and diff != last:
                last = diff
                for j in range(len(ds)):
                    ds[j] -= diff
            else:
                yes = False
                output.append("NO")
                break
        if yes:
            output.append("YES")

for out in output:
    print(out)
