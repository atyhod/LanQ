# import bisect

# n, m = map(int, input().split())

# starts = []
# ends = []

# for _ in range(n):
#     a, b = map(int, input().split())
#     starts.append(a)
#     ends.append(a + b)

# starts.sort()
# ends.sort()

# for _ in range(m):
#     x, y = map(int, input().split())
#     L = x
#     R = x + y

#     left = bisect.bisect_right(ends, L)
#     right = n - bisect.bisect_left(starts, R)

#     print(n - left - right)

n, m = map(int, input().split())
attack = []
for i in range(1, n+1):
    j, k = map(int, input().split())
    attack.append((j,j+k))

for _ in range(m):
    a, b = map(int, input().split())
    b = a + b
    cnt = 0
    for l, r in attack:
        if r <= a or l >= b:
            cnt += 1

    print(n - cnt)