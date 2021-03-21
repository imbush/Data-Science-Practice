t = int(input())
for _ in range(t):
    inputs = [int(x) for x in input().split()]
    n = inputs[0]
    x = inputs[1:]
    side_max = []
    side_min = []
    for i in x:
        if i == 0:
            side_max.append(0)
            side_min.append(0)
        elif i == 1:
            side_max.append(1)
            if n == 2:
                side_min.append(1)
            else:
                side_min.append(0)
        elif i == n:
            side_min.append(2)
            side_max.append(2)
        elif i == n - 1:
            side_min.append(1)
            side_max.append(2)
        else:
            side_min.append(0)
            side_max.append(2)
    works = False
    corners = []
    for i in range(2):
        corners.append(i)
        for j in range(2):
            corners.append(j)
            for k in range(2):
                corners.append(k)
                for l in range(2):
                    corners.append(l)
                    works = True
                    for h in range(4):
                        if not (side_min[h] <= (corners[h] + corners[(h+1) % 4]) <= side_max[h]):
                            works = False
                            break
                    if works:
                        print("YES")
                        break
                    corners.pop()
                if works:
                    break
                corners.pop()
            if works:
                break
            corners.pop()
        if works:
            break
        corners.pop()
    if not works:
        print("NO")