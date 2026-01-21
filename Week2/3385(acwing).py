num = int(input())
val = [0] + list(map(int, input().split()))
tree = [[] for _ in range(num + 1)]
for _ in range(num-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
dp = [0] * (num + 1)
ans = -10000
def dfs(u, parent):
    global ans
    dp[u] = val[u]
    for v in tree[u]:
        if v == parent:
            continue
        dfs(v, u)
        dp[u] += max(0, dp[v])
        ans = max(ans, dp[u])

dfs(1, 1)
print(ans)