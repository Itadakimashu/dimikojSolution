t = int(input())
for i in range(t):
    s = input()
    oc = input()
    count = s.count(oc)
    if count > 0:
        print("Occurrence of '" + oc +  "' in '" +s+"' =" , count)
    else:
        print("'" + oc + "' is not present")