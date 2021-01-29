t = int(input())
output = []
for i in range(t):
    n = int(input())
    nums = [int(x) for x in input().split()]
    max_colors = 0
    current = 1
    last = 0
    for i in range(len(nums)):
        if nums[i] == last:
            current += 1
        else:
            current = 1
        last = nums[i]
        max_colors = max(max_colors, current)
    output.append(max_colors)

for out in output:
    print(out)
