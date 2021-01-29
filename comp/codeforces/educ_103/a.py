t = int(input())
output = []
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    new_k = k
    while new_k < n:
        new_k += k
    k = new_k

    if k % n == 0:
        output.append(k // n)
    else:
        output.append(k // n + 1)
for out in output:
    print(out)