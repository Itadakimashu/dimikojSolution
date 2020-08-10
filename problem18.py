import re
regExVow = re.compile(r'a|e|i|o|u|A|E|I|O|U')
regExCon = re.compile(r'q|w|r|t|y|p|s|d|f|g|h|j|k|l|z|x|c|v|b|n|m|Q|W|R|T|Y|P|S|D|F|G|H|J|K|L|Z|X|C|V|B|N|M')
t = int(input())
for i in range(t):
    s = input()
    vowList = regExVow.findall(s)
    conList = regExCon.findall(s)
    print(''.join(vowList))
    print(''.join(conList))
