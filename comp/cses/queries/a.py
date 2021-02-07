n, q = [int(x) for x in input().split()]
t = [int(x) for x in input().split()]
queries = []
for i in range(q):
    queries.append([int(x) for x in input().split()])

sums = [0]
total = 0
for val in t:
    total += val
    sums.append(total)
for query in queries:
    print(sums[query[1]] - sums[query[0]-1])