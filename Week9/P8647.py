N, K = map(int,input().split())
arr = []
for _ in range(N):
    h, w = map(int,input().split())
    arr.append((h, w))

l, r = 1, max(max(h,w) for h, w in arr)


while l <= r:
    piece = 0
    mid = (l + r) // 2
    for h, w in arr:
        piece += (h//mid) * (w//mid)
    
    if piece < K:
        r = mid - 1
    else:
        ans = mid
        l = mid + 1

print(ans)