arr = []
arr.append(1)
arr.append(2)

n = int(input())
if n > 2:
    for i in range(2, n):
        arr.append(arr[i-1] + arr[i-2])

print(arr[n-1])