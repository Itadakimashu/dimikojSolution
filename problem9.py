import math
t = int(input())
for i in range(t):
    a = int(input())
    sqr = int(math.sqrt(a))
    if a > 1 and sqr * sqr == a:
        print('YES')
    else:
        print('NO')
