t = int(input())
for i in range(t):
    s = input()
    temp = ''
    for j in range(len(s)-1,-1,-1):
        temp += s[j]
    print(temp)
