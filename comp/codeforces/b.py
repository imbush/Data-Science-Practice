def gcd(i: int, j: int) -> int:
    if j == 0:
        return i
    return gcd(j, i % j)


def LCM(s: str, t: str):
    gcd_len = gcd(len(s), len(t))
    new_str = (len(t) // gcd_len) * s
    if new_str == (len(s) // gcd_len) * t:
        return new_str
    else:
        return -1


q = int(input())
prints = []
for i in range(q):
    s = input()
    t = input()
    prints.append(LCM(s, t))
for p in prints:
    print(p)