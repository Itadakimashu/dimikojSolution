def printBox(n):
    for row in range(n):
        for col in range(n):
            print('*',end='')
        print()

t = int(input())
for i in range(t):
    n = int(input())
    printBox(n)
    if i < t-1:
        print()
