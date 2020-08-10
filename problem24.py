t = int(input())
for i in range(t):
    n = int(input())
    list = input().split()
    list2 = []
    for i in range(len(list)):
        if (i+1) % 2 != 0:
            list2.append(list[i])
    print(' '.join(list2))
