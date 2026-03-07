INF = 10**18

n, m ,x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
rev = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    rev[v].append((u, w))

def dijkstra(start, g):
    dist = [INF]*(n+1)
    vis = [False]*(n+1)

    dist[start] = 0

    for _ in range(n):
        u = -1
        mind = INF

        for i in range(1,n+1):
            if not vis[i] and dist[i] < mind:
                mind = dist[i]
                u = i

        if u == -1:
            break

        vis[u] = True

        for v,w in g[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    return dist


dist1 = dijkstra(x, graph)   # x -> i
dist2 = dijkstra(x, rev)     # i -> x

ans = 0
for i in range(1,n+1):
    ans = max(ans, dist1[i] + dist2[i])

print(ans)