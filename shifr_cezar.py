s = input()
s = s.split()
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc = 'abcdefghijklmnopqrstuvwxyz'
sim = '",.!#$%&*+-=?@^_ '
count = 0
s2 = []
result =''
for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j] in ABC:
            count+=1
        if s[i][j] in abc:
            count+=1
    s2.append(count)
    count = 0
for i in range(len(s)):
    result += ' '
    for j in range(len(s[i])):
        if s[i][j] in ABC:
            m = s[i][j]
            n = ABC.find(s[i][j])
            if n + s2[i] > 25:
                result += ABC[s2[i]- (26 - n)]
            else:
                result += ABC[n + s2[i]]
        if s[i][j] in abc:
            m = s[i][j]
            n = abc.find(s[i][j])
            if n + s2[i] > 25:
                result += abc[s2[i] - (26 - n)]
            else:
                result += abc[n + s2[i]]
        if s[i][j] in sim:
            m = s[i][j]
            result += s[i][j]
print(result[1:])