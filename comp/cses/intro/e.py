def main():
    n = int(input())
    if n == 2 or n == 3:
        print("NO SOLUTION")
    elif n == 4:
        print("2 4 1 3")
    else:
        if n % 2 == 1:
            l = [1]
            for i in range(2, n // 2 + 2):
                l.append(i + n // 2)
                l.append(i)
        else:
            l = []
            for i in range(1, n // 2 + 1):
                l.append(i)
                l.append(i + n // 2)
        print(" ".join([str(x) for x in l]))


main()