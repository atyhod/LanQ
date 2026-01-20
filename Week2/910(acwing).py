import sys
from collections import defaultdict

# 4x4 网格，云左上角位置编号 (r, c) -> id
# r, c ∈ [0..2]
def pos_id(r, c):
    return r * 3 + c

def id_pos(pid):
    return divmod(pid, 3)

# 预计算：每个云位置覆盖的 4 个格子
cloud_cells = []
for r in range(3):
    for c in range(3):
        cells = []
        for dr in range(2):
            for dc in range(2):
                cells.append((r + dr) * 4 + (c + dc))
        cloud_cells.append(cells)

# 预计算：云的可移动位置
moves = []
for pid in range(9):
    r, c = id_pos(pid)
    nxt = set()
    nxt.add(pid)  # 不动
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        for step in [1,2]:
            nr, nc = r + dr * step, c + dc * step
            if 0 <= nr <= 2 and 0 <= nc <= 2:
                nxt.add(pos_id(nr, nc))
    moves.append(list(nxt))

CENTER = pos_id(1, 1)  # 初始位置 (1,1)

while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    N = int(line)
    if N == 0:
        break

    festival = []
    for _ in range(N):
        festival.append(list(map(int, sys.stdin.readline().split())))

    # ---------- 第一天初始化 ----------
    bad = False
    dry0 = [1] * 16
    for cell in cloud_cells[CENTER]:
        if festival[0][cell] == 1:
            bad = True
            break
        dry0[cell] = 0

    if bad:
        print(0)
        continue

    # dp: {(cloud_pos, dry_tuple)}
    cur = {(CENTER, tuple(dry0))}

    # ---------- 按天推进 ----------
    for day in range(1, N):
        nxt_states = dict()
        for pos, dry in cur:
            for np in moves[pos]:
                rain = set(cloud_cells[np])
                ok = True
                ndry = [0] * 16
                for i in range(16):
                    if i in rain:
                        if festival[day][i] == 1:
                            ok = False
                            break
                        ndry[i] = 0
                    else:
                        ndry[i] = dry[i] + 1
                        if ndry[i] >= 7:
                            ok = False
                            break
                if not ok:
                    continue
                key = (np, tuple(ndry))
                nxt_states[key] = True
        cur = nxt_states
        if not cur:
            break

    print(1 if cur else 0)
