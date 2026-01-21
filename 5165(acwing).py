W = input()
R = int(input())
C = int(input())

grid = [input().split() for _ in range(R)]
L = len(W)

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),(-1, -1), (-1, 1), (1, -1), (1, 1)]

def in_grid(x, y):
    return 0 <= x < R and 0 <= y < C

ans = 0

for i in range(R):
    for j in range(C):
        if grid[i][j] != W[0]:
            continue
        # 直线
        for dx, dy in dirs:
            x, y = i, j
            ok = True
            for k in range(1, L):
                x += dx
                y += dy
                if not in_grid(x, y) or grid[x][y] != W[k]:
                    ok = False
                    break
            if ok:
                ans += 1

        # 转弯
        for dx1, dy1 in dirs:
            x, y = i, j
            for k in range(1, L - 1):
                x += dx1
                y += dy1
                if not in_grid(x, y) or grid[x][y] != W[k]:
                    break

                # 在 (x,y) 处转弯
                for dx2, dy2 in dirs:
                    if dx1 * dx2 + dy1 * dy2 != 0:
                        continue

                    xx, yy = x, y
                    ok = True
                    for t in range(k + 1, L):
                        xx += dx2
                        yy += dy2
                        if not in_grid(xx, yy) or grid[xx][yy] != W[t]:
                            ok = False
                            break
                    if ok:
                        ans += 1

print(ans)
