t = int(input())
output = []
for i in range(t):
    s = list(input())
    for j in range(len(s)):
        if j % 2 == 0:
            if s[j] == "a":
                s[j] = "b"
            else:
                s[j] = "a"
        else:
            if s[j] == "z":
                s[j] = "y"
            else:
                s[j] = "z"
    output.append("".join(s))
for out in output:
    print(out)