t = int(input())
outs = []
for _ in range(t):
    n, l, r, s = map(int, input().split())
    diff = r - l + 1
    if n * (n + 1) // 2 - (n - diff) * (n - diff + 1) // 2 >= s >= diff * (diff + 1) // 2:
        permutation = list(range(1, n + 1))
        diff = sum(permutation[l-1: r]) - s
        r2 = r - 1  # Backup
        r -= 1
        l -= 1
        i = 0
        while diff > 0:    # Too big
            if diff >= r - i:  # Difference is larger than largest move
                permutation[r], permutation[i] = permutation[i], permutation[r]     # Switch largest with smallest
                diff -= r - i
            elif r - diff < l:   # Last move if viable
                permutation[r], permutation[r - diff] = permutation[r - diff], permutation[r]
                break
            r -= 1
            i += 1
        i = n - 1
        while diff < 0:     # Too small
            if diff <= l - i:
                permutation[l], permutation[i] = permutation[i], permutation[l]
                diff += i - l
            elif l - diff > r:
                permutation[l], permutation[l - diff] = permutation[l - diff], permutation[l]
                break
            l += 1
            i += 1
        outs.append(permutation)
    else:
        outs.append([-1])
for out in outs:
    print(*out)
