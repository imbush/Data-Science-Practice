t = int(input())

for a in range(t):
    n = int(input())
    initial = [int(x) for x in input().split()]
    final = []
    j = 0
    i = 0
    cando = True
    while i < len(initial) and j < len(initial):
        i = j
        while i < len(initial) and j < len(initial) and initial[i] == initial[j]:
            j += 1
        if i == j - 1:
            print(-1)
            cando = False
            break
        else:
            final.append(j)
            for ind in range(i+1, j):
                final.append(ind)
    if cando:
        print(*final)
