s1 = [['Зенит', '3', 'Спартак', '1'], ['Спартак', '1', 'ЦСКА', '1'], ['ЦСКА', '0', 'Зенит', '2'], ['Алания', '4', 'Зенит', '2'], ['Алания', '3', 'Спартак', '2'], ['Алания', '2', 'ЦСКА', '1']]
s2 = {}
for i in range(len(s1)):
    a = s1[i][0]
    b = s1[i][1]
    c = s1[i][2]
    d = s1[i][3]
    s2[s1[i][0]] = int(s1[i][1])
    s2[s1[i][2]] = int(s1[i][3])
print(s2)
s3 = []
s4 = []
for i in range(len(s1)):
    a = s1[i][0]
    s3.append(a)
    b = int(s1[i][1])
    s3.append(b)
    c = s1[i][2]
    s3.append(c)
    d = int(s1[i][3])
    s3.append(d)
    s4.append(s3)
    s3 = []
print(s4)
igr = 0
for i in range(len(s4)):
    for j in range(len(s4[i])):
        for k in range(len(s4[i])):
            if s4[i][j] == s4[i][k]:
                igr +=0
                if s4[i][j] in s2:
                    s2[s4[i][j]] = [igr]
                    igr = 0
a = [0,0,0,0]
for key in s2:
    s2[key] +=a
print(s2)

for i in range(len(s4)):
    a = s4[i][2]
    b = s4[i][0]
    if s4[i][1]< s4[i][3]:
        s2[s4[i][2]][1] += 1
        s2[s4[i][2]][4] += 3
        s2[s4[i][0]][3] += 1
        s2[s4[i][0]][0] += 1
        s2[s4[i][2]][0] += 1
    if s4[i][1]> s4[i][3]:
        s2[s4[i][0]][1] += 1
        s2[s4[i][0]][4] += 3
        s2[s4[i][2]][3] += 1
        s2[s4[i][0]][0] += 1
        s2[s4[i][2]][0] += 1
    if s4[i][1] == s4[i][3]:
        s2[s4[i][0]][2] += 1
        s2[s4[i][2]][2] += 1
        s2[s4[i][0]][4] += 1
        s2[s4[i][2]][4] += 1
        s2[s4[i][0]][0] += 1
        s2[s4[i][2]][0] += 1
print(s2)

for key, value in s2.items():
    print(key+':',end='')
    print(*value)