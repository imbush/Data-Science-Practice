t = int(input())
inputs = []
for i in range(t):
    inputs.append(int(input()))

for n in inputs:
    if n // 2020 >= n % 2020:
        print("YES")
    else:
        print("NO")
