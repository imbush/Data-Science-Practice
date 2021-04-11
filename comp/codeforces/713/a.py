t = int(input())
outs = []
for _ in range(t):
    n = input()
    a = list(map(int, input().split()))
    if a[0] != a[1]:
        correct = a[2]
    else:
        correct = a[0]
    for i in range(len(a)):
        if a[i] != correct:
            outs.append(i+1)
            break
for out in outs:
    print(out)