t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input()))
    if sum(s) % 2 != 0 or s[0] != 1 or s[-1] != 1:
        print("NO")
    else:
        a = ["-"] * n
        b = ["-"] * n
        i = 0
        j = n - 1
        a_open = 0
        off = 0
        while i < j:
            while i != j and not s[i]:
                if off % 2:
                    a[i] = "("
                    b[i] = ")"
                    off += 1
                else:
                    a[i] = ")"
                    b[i] = "("
                    off += 1
                i += 1

            if i != j:
                a[i] = "("
                b[i] = "("
            while i != j and not s[j]:
                if off % 2:
                    a[j] = "("
                    b[j] = ")"
                    off += 1
                else:
                    a[j] = ")"
                    b[j] = "("
                    off += 1
                j -= 1
            if i != j:
                a[j] = ")"
                b[j] = ")"
            j -= 1
            i += 1
        if i == j:
            if off % 2:
                a[j] = "("
                b[j] = ")"
                off += 1
            else:
                a[j] = ")"
                b[j] = "("
                off += 1
        print("YES")
        print("".join(a))
        print("".join(b))

