from collections import deque

n, k = map(int, input().split())
w = list(map(int, input().split()))
w = [0] + w

t = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    t[a].append(b)
    t[b].append(a)

# BFS
dist = [-1] * (n+1)
dist[1] = 0

q = deque([1])

while q:
    u = q.popleft()
    
    # 走1步
    for v in t[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)
    
    # 走2步
    for v in t[u]:
        for vv in t[v]:
            if vv != u and dist[vv] == -1:
                dist[vv] = dist[u] + 1
                q.append(vv)

# 统计答案
ans = 0
for i in range(1, n+1):
    if dist[i] != -1 and dist[i] <= k:
        ans += w[i]

print(ans)