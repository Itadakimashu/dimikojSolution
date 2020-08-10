import math
t = int(input())
for i in range(t):
    n = int(input())
    fac = str(math.factorial(n))
    zero = 0
    for i in range(len(fac)-1,0,-1):
        if fac[i] != '0':
            break
        zero += 1
    print(zero)