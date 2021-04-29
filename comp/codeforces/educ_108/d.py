n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

prods = []
for i in range(n):
    prods.append(a[i] * b[i])

max_diff = 0
for cent in range(n):
    diff = 0
    i = cent-1
    j = cent+1
    while i >= 0 and j < n:
        diff += a[i] * b[j] + b[i] * a[j] - prods[i] - prods[j]
        max_diff = max(diff, max_diff)
        i -= 1
        j += 1

for cent in range(n):
    diff = 0
    i = cent
    j = cent + 1
    while i >= 0 and j < n:
        diff += a[i] * b[j] + b[i] * a[j] - prods[i] - prods[j]
        max_diff = max(diff, max_diff)
        i -= 1
        j += 1

print(sum(prods) + max_diff)
