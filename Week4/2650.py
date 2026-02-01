import bisect

n, m = map(int, input().split())

starts = []
ends = []

for _ in range(n):
    a, b = map(int, input().split())
    starts.append(a)
    ends.append(a + b)

starts.sort()
ends.sort()

for _ in range(m):
    x, y = map(int, input().split())
    L = x
    R = x + y

    left = bisect.bisect_right(ends, L)
    right = n - bisect.bisect_left(starts, R)

    print(n - left - right)
