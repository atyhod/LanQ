import math
n, m = map(int, input().split())
if m > n + 1:
    print(0)
else:
    ans = math.factorial(n) * (math.comb(n+1, 2)*2 * math.comb(n+3, m) + math.comb(n+1, 1) * 2 * m * math.comb(n+2, m-1))
    print(ans)