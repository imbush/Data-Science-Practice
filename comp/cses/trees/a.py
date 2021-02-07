n = int(input())
bosses = [-1]
bosses.extend([int(x) - 1 for x in input().split()])
subs = [0] * n
for boss in bosses:
    while boss >= 0:
        subs[boss] += 1
        boss = bosses[boss]
print(" ".join(map(str, subs)))
