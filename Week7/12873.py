n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [0]*(n+1)

def dfs(u,parent):
    for v in tree[u]:
        if v == parent:
            continue
        dp[v] = dp[u] + 1
        dfs(v,u)

dfs(1,-1)

maxi = -1
max_index = 1

for i in range(1,n+1):
    if dp[i] > maxi:
        maxi = dp[i]
        max_index = i

dp = [0]*(n+1)

dfs(max_index,-1)

d = max(dp)

if d%2:
    d -= 1

print(d)