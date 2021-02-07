import sys
n = int(input())
sys.stdout.flush()
first = 0
last = n+1
while True:
    i = (first + last) // 2
    if i == 1 or i == n:
        print("!", i, "\n")
        break
    k = int(input("? " + str(i) + "\n"))
    sys.stdout.flush()
    if k > int(input("? " + str(i+1) + "\n")):
        sys.stdout.flush()
        first = i
    else:
        sys.stdout.flush()
        k1 = int(input("? " + str(i-1) + "\n"))
        sys.stdout.flush()
        if k > k1:
            last = i
        else:
            print("!", i, "\n")
            break
