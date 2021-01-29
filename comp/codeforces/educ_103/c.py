t = int(input())
output = []
for _ in range(t):
    n = int(input())
    c_list = [int(c) for c in input().split()]
    a_list = [int(a) for a in input().split()]
    b_list = [int(b) for b in input().split()]
    longest = 0
    current = 0
    for i in range(1, n):
        if a_list[i] == b_list[i]:
            current = c_list[i] + 1
        else:
            insides = abs(a_list[i] - b_list[i]) - 1
            current = max(current - insides + c_list[i], insides + 2 + c_list[i])
        longest = max(longest, current)
    output.append(longest)

for out in output:
    print(out)