import math

x0, y0 = map(int, input().split())

if y0 % x0 != 0:
    print(0)
    exit()

n = y0 // x0
ans = 0

for a in range(1, int(math.sqrt(n)) + 1):
    if n % a == 0:
        b = n // a
        if math.gcd(a, b) == 1:
            if a == b:
                ans += 1
            else:
                ans += 2

print(ans)
