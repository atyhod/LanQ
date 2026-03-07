N = int(input())
dp = [dict() for _ in range(N + 1)]

dp[0][1] = 0

for i in range(1, N+1):
    k = int(input())
    for l in range(1, k + 1):
        arr = list(map(int, input().split()))
        j = 0
        while arr[j] != 0:

            prev_planet = arr[j]
            cost = arr[j + 1]

            new_cost = dp[i - 1][prev_planet] + cost
            if new_cost < cost:
                cost = new_cost

            j += 2
        
        dp[i][l] = cost
print(min(dp[3]))