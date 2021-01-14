def main():
    n = int(input().split()[1])
    coins = [int(i) for i in input().split()]
    coins.sort()
    min_coin = coins[0]
    ways = [0 for _ in range(n + 1)]
    for i in range(0, len(ways) - min_coin):
        if ways[i] != 0 or i == 0:
            for j in range(len(coins)):
                if coins[j] + i > n:
                    break
                elif ways[coins[j] + i] == 0:
                    ways[coins[j] + i] = ways[i] + 1
                elif ways[coins[j] + i] > ways[i] + 1:
                    ways[coins[j] + i] = ways[i] + 1
    if ways[-1]:
        print(ways[-1])
    else:
        print(-1)


main()
