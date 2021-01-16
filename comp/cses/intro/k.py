import sys
for i in range(int(input())):
    a, b = map(int,input().split())
    print("YES" if (2 * a - b) % 3 == 0 and 2 * a >= b else "NO")