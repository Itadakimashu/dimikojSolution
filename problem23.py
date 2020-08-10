t = int(input())
for i in range(t):
    s = input()
    sout = ''
    for i in s:
        sout += str(ord(i)-ord('A')+1)
    print(sout)
