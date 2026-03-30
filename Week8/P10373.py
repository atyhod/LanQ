import math

q = int(input())

for _ in range(q):
    x = int(input())
    k = int(math.cbrt(x + 0.5))

    while (k + 1) ** 3 <= x:
        k += 1
    while k ** 3 > x:
        k -= 1

    res = 0
    for i in range(1, k):
        res += i * ((i+1)**3 - i**3)
    res += k * (x - k**3 + 1)
    print(res)