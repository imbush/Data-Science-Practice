def max_min(l1: list, l2: list, diff: int):
    minimum = 0
    maximum = 0
    for i in range(len(l1)):
        if l1[i] < minimum:
            minimum = l1[i]
        if l1[i] > maximum:
            maximum = l1[i]
    for i in range(len(l2)):
        if l2[i] - diff < minimum:
            minimum = l2[i] - diff
        if l2[i] - diff > maximum:
            maximum = l2[i] - diff

    return maximum - minimum


t = int(input())
prints = []
for i in range(t):
    n, m = [int(x) for x in input().split()]

    inst = input()
    sums = [0]
    k = 0
    for i in range(len(inst)):
        if inst[i] == "+":
            k += 1
        else:
            k -= 1
        sums.append(k)

    for j in range(m):
        l, r = [int(x) for x in input().split()]
        prints.append(max_min(sums[:l], sums[r + 1:], sums[r] - sums[l - 1]) + 1)
for p in prints:
    print(p)