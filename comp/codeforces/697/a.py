t = int(input())
inputs = []
for i in range(t):
    inputs.append(int(input()))

for n in inputs:
    if 140737488355328 % n == 0:  # 2 ** 47 > 10 ** 14
        print("NO")
    else:
        print("YES")