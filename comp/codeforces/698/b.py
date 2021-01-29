t = int(input())
output = []
for i in range(t):
    d = int(input().split()[1])
    for num in input().split():
        num = int(num)
        if num >= d * 10 or num % d == 0:
            output.append("YES")
        elif num == 2 or num == 5:
            output.append("NO")
        else:
            test = [False] * (num + 1)
            test[0] = True
            for i in range(len(test)):
                if test[i]:
                    for j in range(d, d * 10, 10):
                        try:
                            test[i + j] = True
                        except IndexError:
                            break
            if test[-1]:
                output.append("YES")
            else:
                output.append("NO")

for out in output:
    print(out)
