t = int(input())
outs = []
for _ in range(t):
    a, b = list(map(int, input().split()))
    s = list(input())
    palindrome = True
    for i in range(len(s)):
        if s[i] == "?":
            # print(i, s)
            if s[i] != s[len(s) - i - 1]:
                s[i] = s[len(s) - i - 1]
        else:
            if s[i] != s[len(s) - i - 1] and s[len(s) - i - 1] != "?":
                outs.append(-1)
                palindrome = False
                break
    if palindrome:
        count_a = s.count("0")
        count_b = s.count("1")
        if count_a <= a and count_b <= b:
            for i in range(len(s)):
                if s[i] == "?":
                    if s[i] == s[len(s) - i - 1]:
                        if a-count_a > b-count_b:
                            s[i] = "0"
                            s[len(s) - i - 1] = "0"
                            count_a += 2
                        else:
                            s[i] = "1"
                            s[len(s) - i - 1] = "1"
                            count_b += 2
                
            if count_a != a and count_b != b:
                outs.append(-1)
            else:
                outs.append("".join(s))
        else:
            outs.append(-1)
for out in outs:
    print(out)
