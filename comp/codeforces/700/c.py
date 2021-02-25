import sys


def main():
    n = int(input())
    sys.stdout.flush()
    # if n == 2:
    #     first = int(input("? 1\n"))
    #     sys.stdout.flush()
    #     second = int(input("? 2\n"))
    #     sys.stdout.flush()
    #     if first > second:
    #         print("! 2\n")
    #         return
    #     else:
    #         print("! 1\n")
    #         return
    first = 0
    last = n+1
    while True:
        i = (first + last) // 2
        if i == 1 or i == n:  # Not always true, see test case 54 and 55
            print("!", i, "\n")
            return
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
                return


main()
