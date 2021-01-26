def p(test: list, d):
    minimum = 101
    next_minimum = 101
    not_over = True
    for i in range(len(test)):
        if test[i] > d:
            not_over = False
        if test[i] < minimum:
            next_minimum = minimum
            minimum = test[i]
        elif test[i] < next_minimum:
            next_minimum = test[i]
    if not_over or (minimum + next_minimum <= d):
        return "YES"
    return "NO"

t = int(input())
prints = []
for i in range(t):
    d = int(input().split()[1])
    test = [int(x) for x in input().split()]
    prints.append(p(test, d))
for pri in prints:
    print(pri)