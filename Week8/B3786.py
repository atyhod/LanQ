def if_lucky(num):
    arr = str(num)
    sum_1 = 0
    sum_2 = 0
    
    for i in range(0, len(arr), 2):
        sum_1 += int(arr[i])
        if i+1 <= len(arr)-1:
            sum_2 += int(arr[i+1])

    if sum_1 == sum_2:
        return True
    return False
# print(if_lucky(121))

a, b = map(int, input().split())
sum = 0
for i in range(a, b+1):
    if if_lucky(i) == True:
        sum += 1

print(sum)