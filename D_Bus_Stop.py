n, m = map(int, input().split())
groups = list(map(int, input().split()))

buses = 0

current = 0
for g in groups:
    if g + current < m:
        current += g
    elif g + current == m:
        current = 0
        buses += 1
    else:
        buses += 1
        current = g


if current > 0:
    buses += 1

print(buses) 