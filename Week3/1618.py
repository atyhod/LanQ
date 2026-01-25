A, B, C = map(int, input().split())

found = False

for k in range(1, 1000):
    X = A * k
    Y = B * k
    Z = C * k

    if X > 999 or Y > 999 or Z > 999:
        break

    s = str(X) + str(Y) + str(Z)

    if len(s) == 9 and set(s) == set('123456789'):
        print(X, Y, Z)
        found = True

if not found:
    print("No!!!")
