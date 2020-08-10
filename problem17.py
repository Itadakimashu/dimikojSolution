import re
regEx = re.compile(r'a|e|i|o|u|A|E|I|O|U')
t = int(input())
for i in range(t):
    s = input()
    print('Number of vowels =' , len(regEx.findall(s)))
