t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    if n == 1:
        print(*l)
    else:
        news_i = []
        current_max = 0
        for j in range(len(l)):
            if l[j] > current_max:
                news_i.append(j)
                current_max = l[j]
        new_l = []
        last = n
        while last != 0:
            new_l.extend(l[news_i[-1]:last])
            last = news_i.pop()
        print(*new_l)