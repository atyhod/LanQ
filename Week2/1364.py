n = int(input())

w = [0] * (n + 1)
g = [[] for _ in  range(n+1)]

for i in range(1, n+1):
    w[i], u, v = map(int, input().split())
    
    if u != 0:
        g[i].append(u)
        g[u].append(i)

    if v != 0:
        g[i].append(v)
        g[v].append(i)

def dfs(curr, parent, dist):
    total = w[curr] * dist
    for i in g[curr]:
        if i != parent:
            total += dfs(i, curr, dist + 1)
    return total

min = dfs(1, 1, 0)
for i in range(2, n+1):
    total = dfs(i, i, 0)
    if total < min:
        min = total
print(min)