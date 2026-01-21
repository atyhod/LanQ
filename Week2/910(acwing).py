pos = [6, 7, 10, 11]
method = 0
def judge(pos, event):
    for i in range (0, 4):
        if event[pos[i]] == 1:
            return -1
        
def move(direction, pos, rate):
    len = rate * 4
    if direction == 'up' & (pos[0] - 1)//4 < rate:
        return -1
    if direction == 'down' & (20 - pos[2])//4 < rate:
        return -1
    if direction == 'left' & (pos[0] - 1)%4 < rate:
        return -1
    if direction == 'right' & (3-(pos[1]-1)%4) < rate:
        return -1
    
    for i in range(0,4):
        if direction == 'up':
            pos[i] -= len
        if direction == 'down':
            pos[i] += len
        if direction == 'left':
            pos[i] -= rate
        if direction == 'right':
            pos[i] += rate

    return pos

        
day = int(input())
while day != 0:
    event = []
    event = list(map(int, input().split()))
    event = [0] + event
    for _ in range(day):
        if judge(pos, event) == -1:
            pass