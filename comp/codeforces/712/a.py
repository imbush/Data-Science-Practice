t = int(input())
for _ in range(t):
    s = input()
    not_found = True
    for i in range(len(s)):
        if s[i] != "a":
            if i == 0:
                print("YES")
                print(s + "a")
            else:
                print("YES")
                print(s[:-i] + "a" + s[-i:])
            not_found = False
            break
    if not_found:
        print("NO")