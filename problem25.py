def lcm(n,m):
    greater = max(n,m)
    while True:
        if greater % n == 0 and greater % m == 0:
            return greater
        greater += 1

t = int(input())
for i in range(t):
    a,b = input().split()
    n,m = int(a),int(b)
    print('LCM =',lcm(n,m))
