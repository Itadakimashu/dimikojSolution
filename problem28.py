import copy
n = int(input())
ara = [0 for i in range(n)]
for i in range(n):
    ara[i] = int(input())
ara2 = copy.copy(ara)
ara2.sort()
if ara == ara2:
    print('YES')
else:
    print('NO')
