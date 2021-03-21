t = int(input())
for _ in range(t):
    a = input()
    if a[0] == a[-1]:
        print("NO")
        continue
    l1 = {a[0]: 1, a[-1]: 0}
    l2 = {a[0]: 1, a[-1]: 0}
    for char in ["A", "B", "C"]:
        if char not in l1:
            l1[char] = 0
            l2[char] = 1
    case1 = 0
    for i in range(len(a)):
        if l1[a[i]] == 1:
            case1 += 1
        else:
            case1 -= 1
        if case1 < 0:
            break
    if case1 == 0:
        print("YES")
        continue
    case2 = 0
    for i in range(len(a)):
        if l2[a[i]] == 1:
            case2 += 1
        else:
            case2 -= 1
        if case2 < 0:
            break
    if case2 == 0:
        print("YES")
    else:
        print("NO")
