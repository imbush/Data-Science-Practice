n, q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
num_ones = sum(a)
for _ in range(q):
    t, k = [int(x) for x in input().split()]
    if t == 1:
        a[k-1] = 1 - a[k-1]
        if a[k-1] == 1:
            num_ones += 1
        else:
            num_ones -= 1
    else:
        if k > num_ones:
            print(0)
        else:
            print(1)
