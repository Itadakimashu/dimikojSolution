t = int(input())
for i in range(t):
    a,b,c = input().split()
    l = [int(a),int(b),int(c)]
    l.sort()
    print('Case ' + str(i+1) + ': ' + str(l[0]) + ' ' + str(l[1]) + ' ' + str(l[2]))
