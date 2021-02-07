import math
t = int(input())
output = []
for i in range(t):
    a, b, n = [int(x) for x in input().split()]
    la = [int(x) for x in input().split()]
    lb = [int(x) for x in input().split()]
    dam = 0
    for i in range(n):
        dam += la[i] * math.ceil(lb[i] / a)
    if dam >= b + max(la):
        output.append("NO")
    else:
        output.append("YES") 


for out in output:
    print(out)