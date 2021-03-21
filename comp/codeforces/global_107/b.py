t = int(input())
for _ in range(t):
    n, u, v = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    this = True
    for i in range(1, n):
        if a[i] != a[i-1]:
            print(min(u, v))
            this = False
    if this:
        print(min(u + v, 2 * v))

l = k;
                    while (l < n) {
                        s[l] --;
                        l += s[l];
                        s[l] = max(1, s[l]);
                        l ++;
                    }