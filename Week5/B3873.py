N, L = map(int,input().split())
drinks = [tuple(map(int, input().split())) for _ in range(N)]

INF = 10**30
dp = [INF] *  (L + 1)
dp[0] = 0

for cost, volumn in drinks:
    for i in range(L, -1, -1):
        if dp[i] == INF:
            continue
        new_v = min(L, i + volumn)
        dp[new_v] = min(dp[new_v], dp[i] + cost)

if dp[L] == INF:
    print("no solution")
else:
    print(dp[L])