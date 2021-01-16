# def max_min(l1: list, l2: list, diff: int):
#     minimum = 0
#     maximum = 0
#     for i in range(len(l1)):
#         if l1[i] < minimum:
#             minimum = l1[i]
#         if l1[i] > maximum:
#             maximum = l1[i]
#     for i in range(len(l2)):
#         if l2[i] - diff < minimum:
#             minimum = l2[i] - diff
#         if l2[i] - diff > maximum:
#             maximum = l2[i] - diff

#     return maximum - minimum


t = int(input())
prints = []
for i in range(t):
    n, m = [int(x) for x in input().split()]

    inst = input()
    sums = [[0, 0, 0]]  #x, max from left, min from left, max from right, min from left
    x = 0
    r = 0
    lmax = 0
    lmin = 0
    for i in range(len(inst)):
        if inst[i] == "+":
            x += 1
        else:
            x -= 1

        if x > lmax:
            lmax = x
        elif x < lmin:
            lmin = x
        sums.append([x, lmax, lmin])
    print(sums)
    rmax = 0
    rmin = 0
    for i in range(len(inst)):
        if sums[-1 - i][0] > rmax:
            sums = sums[-1 - i][0]
        elif sums[-1 - i][0] < rmin:
            rmin = sums[-1 - i][0]
        print(-i - 1, sums[-i - 1])
        sums[-i - 1].append(rmax)
        sums[-i - 1].append(rmin)
    print(sums)

    for j in range(m):
        left, right = [int(x) for x in input().split()]
        diff = sums[right][0] - sums[left - 1][0]
        dist = max(sums[left - 1][1], sums[right][3] - diff) - min(sums[left - 1][2], sums[right][4] - diff)
        prints.append(dist + 1)


for p in prints:
    print(p)
