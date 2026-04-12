n = int(input())
fama = list(map(int, input().split()))

s = sum(fama)

dp = [False] *  (2*s+1)
dp[s] = True

for w in fama:
    ndp = dp[:]
    for i in range(2*s+1):
        if dp[i]:
            if i + w <= 2*s:
                ndp[i + w] = True
            if i - w >= 0:
                ndp[i - w] = True
    dp = ndp

ans = set()

for i in range(2*s + 1):
    if dp[i]:
        weight = abs(i - s)
        if weight != 0:
            ans.add(weight)

print(len(ans))