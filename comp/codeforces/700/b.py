import math
t = int(input())
output = []
for i in range(t):
    a, b, n = [int(x) for x in input().split()]
    la = [int(x) for x in input().split()]
    lb = [int(x) for x in input().split()]
    dam = 0
    maximum = 0
    for i in range(n):
        maximum = max(maximum, la[i])
        dam += la[i] * ((lb[i] + a - 1) // a)
    if dam >= b + maximum:
        output.append("NO")
    else:
        output.append("YES")

for out in output:
    print(out)
