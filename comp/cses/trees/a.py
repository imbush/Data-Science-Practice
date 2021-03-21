n = int(input())
bosses = [int(x) - 1 for x in input().split()]
subs = [0] * n
for i in range(n-1, 0, -1):
    subs[bosses[i - 1]] += subs[i] + 1
print(*subs)
