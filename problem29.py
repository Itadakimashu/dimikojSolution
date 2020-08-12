t = int(input())
for i in range(t):
    ch = input()
    if ch >= '1' and ch <= '9':
        print('Numerical Digit')
    elif ch >= 'a' and ch <= 'z':
        print('Lowercase Character')
    elif ch >= 'A' and ch <= 'Z':
        print('Uppercase Character')
    else:
        print('Special Character')
