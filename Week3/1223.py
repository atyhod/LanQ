n = int(input())
T = list(map(int, input().split()))
people = [(T[i], i+1) for i in range(n)]

people.sort()

order = []
time = 0

for i in range(n):
    order.append(str(people[i][1]))
    time += (n-1-i) * people[i][0]

print(" ".join(order))
print(f"{time / n:.2f}")
