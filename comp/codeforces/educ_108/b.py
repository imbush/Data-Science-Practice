t = int(input())
for _ in range(t):
    n, m, k = list(map(int, input().split()))
    if k == m * n - 1:
        print("YES")
    else:
        print("NO")