t = int(input())
for _ in range(t):
    n = int(input())
    u = list(map(int, input().split()))
    s = list(map(int, input().split()))
    num_unis = max(u)
    teams = [[] for _ in range(num_unis)]
    for i in range(n):
        teams[u[i] - 1].append(s[i])

    for i in range(len(teams)):
        teams[i].sort()

    cum_sums = [[0] for _ in range(num_unis)]
    for i in range(num_unis):
        cum_sum = 0
        for j in range(len(teams[i])):
            cum_sum += teams[i][j]
            cum_sums[i].append(cum_sum)

    strengths = [sum(team) for team in teams]
    output = [0] * n
    for i in range(1, n + 1):
        for team_i in range(len(teams)):
            remainder = len(teams[team_i]) % i
            if remainder < len(teams[team_i]):
                output[i-1] += strengths[team_i] - cum_sums[team_i][remainder]
    print(*output)