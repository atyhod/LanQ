n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
m = int(input())

p1 = p2 = p3 = 0
ans = 0

for _ in range(m):
    x1, x2, x3 = map(int, input().split())
    p1 = (p1 + x1) % n
    p2 = (p2 + x2) % n
    p3 = (p3 + x3) % n

    A, B, C = a[p1], b[p2], c[p3]

    if A == B == C:
        ans += 200
    elif B == A + 1 and C == B + 1:
        ans += 200
    elif sorted([A, B, C]) in ([1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7],[6,7,8],[7,8,9]):
        ans += 100
    elif A == B or A == C or B == C:
        ans += 100

print(ans)