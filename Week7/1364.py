n = int(input())
total = 0

w = [0] * (n + 1)
tree = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    weight, left, right = map(int, input().split())
    w[i] = weight
    total += w[i]

    if left != 0:
        tree[i].append(left)
        tree[left].append(i)
        
    if right != 0:
        tree[i].append(right)
        tree[right].append(i)

distance = [0] * (n + 1)
size = [0] * (n + 1)

def dfs1(u, parent, depth):
    size[u] = w[u]
    distance[1] += w[u] * depth
    for i in tree[u]:
        if i == parent:
            continue
        dfs1(i, u, depth + 1)
        size[u] += size[i]

dfs1(1, 0, 0)

def dfs2(u, parent):
    for j in tree[u]:
        if j == parent:
            continue
        distance[j] = distance[u] - 2 * size[j] + total
        dfs2(j, u)

dfs2(1, 0)

print(min(distance[1:]))