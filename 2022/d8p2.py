b = p = 0
l = 99
a = []
for i in range(l):
    a.append(input())
for i in range(l):
    for j in range(l):
        b1 = b2 = b3 = b4 = 0
        for k in range(i-1,-1,-1):
            b1 = b1 + 1
            if a[i][j] <= a[k][j]:
                break
        for k in range(j-1,-1,-1):
            b2 = b2 + 1
            if a[i][j] <= a[i][k]:
                break
        for k in range(i+1,l):
            b3 = b3 + 1
            if a[i][j] <= a[k][j]:
                break
        for k in range(j+1,l):
            b4 = b4 + 1
            if a[i][j] <= a[i][k]:
                break
        b = b1 * b2 * b3 * b4
        if b > p:
            p = b
print(p)