t = int(input())
bs = []
for i in range(t):
    n = input()
    bs.append([int(x) for x in input()])

for b in bs:
    a = "1"
    last_sum = b[0]
    for j in range(1, len(b)):
        if b[j] == last_sum:
            a += "0"
            last_sum = b[j] - 1
        else:
            a += "1"
            last_sum = b[j]
    print(a)