import math
t = int(input())
for i in range(t):
    n = input()
    amsNum = 0
    for i in n:
        amsNum += pow(int(i),len(n))
    if amsNum == int(n):
        print(n,'is an armstrong number!')
    else:
        print(n,'is not an armstrong number!')
