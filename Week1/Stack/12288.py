stack = []
n = int(input())
pos = dict()    #dict比list.index()效率高
odd = 0

for _ in range(n):
    num = int(input())
    if num in pos:
        idx = pos[num]

        if idx > 0 and (stack[idx-1] + stack[idx]) % 2 == 1:
            odd -= 1
        if idx < len(stack) - 1 and (stack[idx] + stack[idx+1]) % 2 == 1:
            odd -= 1
        if 0 < idx < len(stack) - 1 and (stack[idx-1] + stack[idx+1]) % 2 == 1:
            odd += 1

        stack.pop(idx)
        del pos[num]

        for k in pos:
            if pos[k] > idx:
                pos[k] -= 1
    if stack:
        if (stack[-1] + num) % 2 == 1:
            odd += 1
    stack.append(num)
    pos[num] = len(stack) - 1

    print(odd)