w = int(input())
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
arr.sort()
arr = [0] + arr

i, j, cnt = 1, n, 0
while i < j:
    sum = arr[i] + arr[j]
    if sum <= w:
        i += 1
        j -= 1
    else:
        j -= 1
    cnt += 1

if i > j:
    print(cnt)
elif i == j:
    print(cnt + 1)