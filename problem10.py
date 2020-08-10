t = int(input())
for i in range(t):
    a,b,c = input().split()
    target,run,ball = int(a)+1,int(b),int(c)
    rr = run /(300-ball)*6
    print("%.2f" % rr,end=' ')
    if target - run < 0:
        print("%.2f" % 0.000)
    else:
        rrr = (target - run)/ball*6
        print("%.2f" % rrr)