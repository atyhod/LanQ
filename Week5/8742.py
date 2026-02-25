n = int(input())
W = list(map(int, input().split()))

dp = {0}
for w in W:
    new_dp = set(dp)
    for i in dp:
        new_dp.add(i + w)
        new_dp.add(abs(i - w))
    dp = new_dp

if 0 in dp:
    dp.remove(0)

print(len(dp))