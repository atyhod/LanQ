n, x = map(int, input().split())
x = str(x)

ans = 0
for i in range(1, n + 1):
    ans += str(i).count(x)

print(ans)
