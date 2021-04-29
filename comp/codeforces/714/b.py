t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    minimum = min(a)
    min_count = a.count(minimum)
    if min_count < 2 or not (n * minimum == sum([(num & minimum) for num in a])):
        print(0)
    else:
        total = 2
        total *= min_count * (min_count - 1) // 2
        for i in range(1, n - 1):
            total = (total * i) % 1000000007
        print(total)
