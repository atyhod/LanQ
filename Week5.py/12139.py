ans = []
grid = [[-1]*6 for _ in range(6)]

def valid(r, c):
    row = grid[r]
    if row.count(1) > 3 or row.count(0) > 3:
        return False
    for i in range(4):
        if row[i] == row[i+1] == row[i+2] != -1:
            return False
    col_vals = [grid[i][c] for i in range(6)]
    if col_vals.count(1) > 3 or col_vals.count(0) > 3:
        return False
    for i in range(4):
        if col_vals[i] == col_vals[i+1] == col_vals[i+2] != -1:
            return False
        
    return True
def dfs(pos=0):
    if pos == 36:
        print("".join(str(grid[i][j]) for i in range(6) for j in range(6)))
        return

    r, c = divmod(pos, 6)
    for val in (0, 1):
        grid[r][c] = val
        if valid(r, c):
            dfs(pos + 1)
    grid[r][c] = -1