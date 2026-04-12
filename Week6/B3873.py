N, L = map(int, input().split())

c = []
l = []
for _ in range(N):
    ci, li = map(int, input().split())
    c.append(ci)
    l.append(li)

INF = 10**18
dp = [INF] * (L + 1)
dp[0] = 0

for i in range(N):
    for j in range(L, -1, -1):
        if dp[j] == INF:
            continue
        nj = min(L, j + l[i])
        dp[nj] = min(dp[nj], dp[j]+c[i])

if dp[L] == INF:
    print("no solution")

else:
    print(dp[L])