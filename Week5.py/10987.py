N, A, B = map(int, input().split())
w = list(map(int, input().split()))

dp = [[False] * (B + 1) for _ in range(A + 1)]
dp[0][0] = True

for weight in w:
    for i in range(A, -1, -1):
        for  j in range(B, -1, -1):
            if dp[i][j]:
                if i + weight <= A:
                    dp[i + weight][j] = True
                if j + weight <= B:
                    dp[i][j + weight] = True

ans = 0
for i in range(A + 1):
    for j in range(B + 1):
        if dp[i][j]:
            ans = max(ans, i + j)
print(ans)