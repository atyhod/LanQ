s = []
l = []
i = int(input())
for _ in range(i):
    book = str(input())
    if book != 'READ':
        s.append(book)
    else:
        print(s.pop())
