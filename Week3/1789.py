n, m, k = map(int, input().split())

light = [[False] * (n+1) for _ in range(n+1)]

def in_grid(x, y):
    return 1 <= x <= n and 1 <= y <= n

torch_dirs = [(0, 0), (0, 1), (0, 2), (0, -1), (0, -2), (1, 0), (2, 0), (-1, 0), (-2, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for _ in range(m):
    x, y = map(int, input().split())
    for dx, dy in torch_dirs:
        if in_grid(x+dx, y+dy):
            light[x+dx][y+dy] = True

for _ in range(k):
    x, y = map(int, input().split())
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            nx, ny = x + dx, y + dy
            if in_grid(nx, ny):
                light[nx][ny] = True

ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if not light[i][j]:
            ans += 1

print(ans)