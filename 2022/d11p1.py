def m0(old):
    return old * 7
def m1(old):
    return old + 7
def m2(old):
    return old * 3
def m3(old):
    return old + 3
def m4(old):
    return old * old
def m5(old):
    return old + 8
def m6(old):
    return old + 2
def m7(old):
    return old + 4

s = [0,0,0,0,0,0,0,0]
m = [0,1,2,3,4,5,6,7]
d = [13,19,5,2,17,11,7,3]
t = [1,2,5,1,6,4,3,4]
f = [3,7,7,2,0,6,0,5]
a = s
a[0] = [64]
a[1] = [60,84,84,65]
a[2] = [52,67,74,88,51,61]
a[3] = [67,72]
a[4] = [80,79,58,77,68,74,98,64]
a[5] = [62,53,61,89,86]
a[6] = [86,89,82]
a[7] = [92,81,70,96,69,84,83]
for i in range(20):
    for j in range(8):
        length = len(a[j])
        for k in range(length):
            if j == m[j]:
                a[j][k] = m0(a[j][k])
                a[j][k] = a[j][k] // 3
                if a[j][k] % d[j] == 0:
                    a[t[j]].append(a[j].pop(0))
                else:
                    a[f[j]].append(a[j].pop(0))
            if j == m[j]:
                a[j][k] = m1(a[j][k])
                a[j][k] = a[j][k] // 3
                if a[j][k] % d[j] == 0:
                    a[t[j]].append(a[j].pop(0))
                else:
                    a[f[j]].append(a[j].pop(0))
            if j == m[j]:
                a[j][k] = m2(a[j][k])
                a[j][k] = a[j][k] // 3
                if a[j][k] % d[j] == 0:
                    a[t[j]].append(a[j].pop(0))
                else:
                    a[f[j]].append(a[j].pop(0))
            if j == m[j]:
                a[j][k] = m3(a[j][k])
                a[j][k] = a[j][k] // 3
                if a[j][k] % d[j] == 0:
                    a[t[j]].append(a[j].pop(0))
                else:
                    a[f[j]].append(a[j].pop(0))
            if j == m[j]:
                a[j][k] = m4(a[j][k])
                a[j][k] = a[j][k] // 3
                if a[j][k] % d[j] == 0:
                    a[t[j]].append(a[j].pop(0))
                else:
                    a[f[j]].append(a[j].pop(0))
            if j == m[j]:
                a[j][k] = m5(a[j][k])
                a[j][k] = a[j][k] // 3
                if a[j][k] % d[j] == 0:
                    a[t[j]].append(a[j].pop(0))
                else:
                    a[f[j]].append(a[j].pop(0))
            if j == m[j]:
                a[j][k] = m6(a[j][k])
                a[j][k] = a[j][k] // 3
                if a[j][k] % d[j] == 0:
                    a[t[j]].append(a[j].pop(0))
                else:
                    a[f[j]].append(a[j].pop(0))
            if j == m[j]:
                a[j][k] = m7(a[j][k])
                a[j][k] = a[j][k] // 3
                if a[j][k] % d[j] == 0:
                    a[t[j]].append(a[j].pop(0))
                else:
                    a[f[j]].append(a[j].pop(0))
                length = len(a[j])
        s[k] = s[k] + 1
s.sort(reverse = False)
print(s[0] * s[1])