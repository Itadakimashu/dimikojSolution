t = int(input())
for i in range(t):
    a = float(input())
    days = 0
    while a > 1.0:
        a /= 2
        days += 1
    print(days,'days')
