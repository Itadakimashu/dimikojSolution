t = int(input())
for i in range(t):
    s = str(input())
    list = s.split(' ')
    whitespace = 0;
    for j in list:
        if j == '':
            whitespace += 1
    print(len(list)-whitespace)