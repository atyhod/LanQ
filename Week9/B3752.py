F = [0, 1, 1]
for i in range(3, 100):
    F.append(F[i-1] + F[i-2])

T = int(input())
for _ in range(T):
    x = int(input())
    res = []
    for n in range(2, len(F)):
        fn_1 = F[n-1]
        fn_2 = F[n-2]
        if fn_1 > x:
            break
        if (x - fn_2) % fn_1 == 0:
            a = (x - fn_2) // fn_1
            if a >= 1:
                res.append((n, a))
    for n, a in res:
        print(n, a)