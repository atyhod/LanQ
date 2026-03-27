def parse(field, lo, hi):
    if field == '*':
        return set(range(lo, hi + 1))
    elif ',' in field:
        return set(map(int, field.split(',')))
    elif '-' in field:
        l, r = map(int, field.split('-'))
        return set(range(l, r + 1))
    else:
        return {int(field)}

s = input().split()

sec = parse(s[0], 0, 59)
minute = parse(s[1], 0, 59)
hour = parse(s[2], 0, 23)
day = parse(s[3], 1, 31)
month = parse(s[4], 1, 12)

days = [31,28,31,30,31,30,31,31,30,31,30,31]

date_cnt = 0
for m in month:
    for d in day:
        if d <= days[m-1]:
            date_cnt += 1

ans = len(sec) * len(minute) * len(hour) * date_cnt

print(ans)