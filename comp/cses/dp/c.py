def main():
    x = int(input().split()[1])
    coins = sorted([int(coin) for coin in input().split()])
    sums = [0] * (x + 1)
    sums[0] = 1
    for i in range(len(sums)):
        for coin in coins:
            # print(sums[i + coin], sums[i])
            try:
                sums[i + coin] = (sums[i + coin] + sums[i]) % 1000000007
            except IndexError:
                break
    print(sums[-1])


main()
