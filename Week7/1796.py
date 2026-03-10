INF = 10000
N = int(input())

prev = [0]
for i in range(1, N+1):
    n = int(input())
    curr = [INF] * n
    for j in range(n):
        arr = list(map(int, input().split()))
        k = 0
        while arr[k] != 0:
            curr[j] = min(curr[j], prev[arr[k]-1] + arr[k+1])
            k += 2

    prev = curr

print(min(curr))