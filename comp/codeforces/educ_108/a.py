t = int(input())
for _ in range(t):
    r, b, d = list(map(int, input().split()))
    r, b = min(r, b), max(r, b)
    diff = b // r
    if b % r == 0:
        diff -= 1
    if diff > d:
        print("NO")
    else:
        print("YES")