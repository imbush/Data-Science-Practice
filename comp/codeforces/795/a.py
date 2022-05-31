t = int(input())
ans = []
for i in range(t):
    n = int(input())
    list1 = [int(x) % 2 == 0 for x in input().split()]
    evens = sum(list1)
    total = len(list1)
    answer = min(evens, total - evens)
    ans.append(answer)

for answer in ans:
    print(answer)
