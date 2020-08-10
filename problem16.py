def rev(s):
    temp = ''
    for i in range(len(s)-1,-1,-1):
        temp += s[i]
    return temp

t = int(input())
for i in range(t):
    list = input().split()
    for i in range(len(list)):
        s = list[i]
        list[i] = rev(s)
    print(' '.join(list))