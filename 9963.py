def can_deliver(n, location, speed):
    current_time = 0
    for i in range(n):
        x, y, distance = location[i]
        travel_time = distance / speed
        current_time += travel_time
        
        if current_time < x:
            current_time = x
        if current_time > y:
            return False
    return True

def min_speed(n, location):
    low, high = 0.0, 1e9
    
    while high - low > 0:
        mid = (low + high) / 2
        if can_deliver(n, location, mid):
            high = mid
        else:
            low = mid
    return (low + high) / 2

n = int(input())
location = []
for _ in range(n):
    x, y, s = map(int, input().split())
    location.append((x, y, s))

result = min_speed(n, location)
print(f"{result:.2f}")
