n = int(input())
arr = list(map(int, input().split()))
k = int(input())

l, r = max(arr), sum(arr)
while l <= r:
    mid = (l + r)//2
    cnt = 1
    sum = 0
    for i in arr:
        if sum + i > mid:
            sum = 0
            cnt += 1
        sum += i
    
    if cnt <= k:
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)