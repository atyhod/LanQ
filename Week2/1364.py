n = int(input())
weight = [0]
t = [[] for _ in range(n+1)]

for i in range(1, n+1):
    w, u, v = map(int, input().split())
    weight.append(w)
    if u != 0:
        t[i].append(u)
        t[u].append(i)
    if v != 0:
        t[i].append(v)
        t[v].append(i)

def dfs(u, parent, dist):
    res = dist * weight[u]
    for v in t[u]:
        if v != parent:
            res += dfs(v, u, dist+1)
    return res

min = dfs(1, 0, 0)
for i in range(1, n+1):
    curr = dfs(i, 0, 0)
    if min > curr:
        min = curr
print(min)