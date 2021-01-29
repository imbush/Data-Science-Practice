def main():
    n = int(input())
    if (n * (n + 1) / 2) % 2 == 1:  # Not possible when sum to n not divisible
        print("NO")
        return

    print("YES")
    if n % 2 == 0:
        half_n = n // 2
        quarter_n_1 = n // 4 + 1
        set1 = list(range(1, quarter_n_1)) + list(range(half_n + quarter_n_1, n + 1))
        set2 = list(range(quarter_n_1, quarter_n_1 + half_n))
    else:
        half_n = (n - 3) // 2
        quarter_n_4 = (n - 3) // 4 + 4
        set1 = [1, 2] + list(range(4, quarter_n_4)) + list(range(half_n + quarter_n_4, n + 1))
        set2 = [3] + list(range(quarter_n_4, quarter_n_4 + half_n))
    print(len(set1))
    print(" ".join([str(i) for i in set1]))
    print(len(set2))
    print(" ".join([str(i) for i in set2]))


main()
