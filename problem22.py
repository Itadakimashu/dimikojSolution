n = 100000
prime = [True for i in range(n+1)]
p = 2
while p * p <= 100000:
    if prime[p] == True:
        for i in range(p * p, n+1, p):
            prime[i] = False
    p += 1
t = int(input())
for i in range(t):
    a,b = input().split()
    n,m = int(a),int(b)
    c = 0
    for j in range(n,m+1):
        if j > 1 and prime[j]:
            c += 1
    print(c)
